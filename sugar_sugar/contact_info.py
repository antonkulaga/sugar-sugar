from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True, slots=True)
class PersonEmail:
    name: str
    email: str


@dataclass(frozen=True, slots=True)
class LinkItem:
    platform: str
    label: str
    url: str


@dataclass(frozen=True, slots=True)
class LinkedInItem:
    name: str
    role: str
    url: str


@dataclass(frozen=True, slots=True)
class ContactInfo:
    study_contacts: list[PersonEmail]
    general_email: Optional[str]
    social_links: list[LinkItem]
    platform_links: list[LinkItem]
    linkedin_contacts: list[LinkedInItem]


_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _project_root() -> Path:
    # Repo layout: <root>/sugar_sugar/<this_file>.py
    return Path(__file__).resolve().parents[1]


def _parse_md_link(cell: str) -> tuple[str, str]:
    m = _MD_LINK_RE.search(cell)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return cell.strip(), cell.strip()


def _parse_md_table(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines:
        s = line.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        # Skip separator row like |----|----|
        if set(s.replace("|", "").replace(" ", "")) <= {"-"}:
            continue
        parts = [p.strip() for p in s.strip("|").split("|")]
        rows.append(parts)
    # Drop header row if present.
    if rows:
        return rows[1:]
    return []


def load_contact_info(path: Optional[Path] = None) -> ContactInfo:
    p = path or (_project_root() / "data" / "glucosedao_contacts.md")
    if not p.exists():
        return ContactInfo(
            study_contacts=[],
            general_email=None,
            social_links=[],
            platform_links=[],
            linkedin_contacts=[],
        )

    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()

    def section_lines(title: str) -> list[str]:
        header = f"## {title}".strip()
        idxs = [i for i, ln in enumerate(lines) if ln.strip() == header]
        if not idxs:
            return []
        start = idxs[0] + 1
        out: list[str] = []
        for ln in lines[start:]:
            if ln.strip().startswith("## "):
                break
            out.append(ln)
        return out

    study_rows = _parse_md_table(section_lines("Study Contacts"))
    study_contacts = [
        PersonEmail(name=row[0], email=row[1])
        for row in study_rows
        if len(row) >= 2 and row[0] and row[1]
    ]

    general_email: Optional[str] = None
    for ln in section_lines("General Team Email"):
        s = ln.strip()
        if "@" in s:
            general_email = s.replace("📧", "").replace("*", "").strip()
            break

    social_rows = _parse_md_table(section_lines("Social Media & Community"))
    social_links: list[LinkItem] = []
    for row in social_rows:
        if len(row) < 2:
            continue
        label, url = _parse_md_link(row[1])
        social_links.append(LinkItem(platform=row[0], label=label, url=url))

    platforms_rows = _parse_md_table(section_lines("Website & Platforms"))
    platform_links: list[LinkItem] = []
    for row in platforms_rows:
        if len(row) < 2:
            continue
        label, url = _parse_md_link(row[1])
        platform_links.append(LinkItem(platform=row[0], label=label, url=url))

    linkedin_rows = _parse_md_table(section_lines("LinkedIn"))
    linkedin_contacts: list[LinkedInItem] = []
    for row in linkedin_rows:
        if len(row) < 3:
            continue
        _, url = _parse_md_link(row[2])
        linkedin_contacts.append(LinkedInItem(name=row[0], role=row[1], url=url))

    return ContactInfo(
        study_contacts=study_contacts,
        general_email=general_email,
        social_links=social_links,
        platform_links=platform_links,
        linkedin_contacts=linkedin_contacts,
    )


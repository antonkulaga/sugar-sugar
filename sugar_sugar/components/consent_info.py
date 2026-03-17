from pathlib import Path
from typing import List

from dash import html

TITLES = {
    # English
    "Participant Information",
    "Predicting Glucose Trends Based on Prior Value Patterns: An Online Benchmarking Study",
    "Short title: Sugar-Sugar Glucose Forecasting Study",
    "How does the study work?",
    "Optional upload of your own CGM data",
    "Voluntary participation",
    "Who can participate?",
    "What possible risks, discomforts, or side effects are associated with participation?",
    "What potential benefits does participation offer?",
    "What rights and conditions are associated with participation?",
    "Data Protection",
    "1. Who is responsible for data processing and storage?",
    "Responsible Institution",
    "2. Who can you contact with questions about the study or data protection?",
    "Study contacts",
    "Data Protection Officer, Rostock University Medical Center",
    "Competent data protection supervisory authority",
    "3. What data do we need from you for the study?",
    "4. Where does this data come from?",
    "5. For what purposes is your data needed, and how is it protected?",
    "6. Where and for how long is data stored?",
    "7. Who has access to your data? Will your data be shared or published?",
    "8. What data protection rights do you have when participating in the study?",
    "Right to withdraw",
    "Declaration of Consent",
    "for participation in the Sugar-Sugar Glucose Forecasting Study",
    "and the associated data processing",
    # German
    "Teilnehmerinformation",
    "Vorhersage des Glukoseverlaufs anhand vorheriger Wertemuster: Eine Online-Benchmarking-Studie",
    "Kurztitel: Sugar-Sugar Glukoseprognose-Studie",
    "Wie läuft die Studie ab?",
    "Optionaler Upload eigener CGM-Daten",
    "Freiwilligkeit der Teilnahme",
    "Wer kann teilnehmen?",
    "Welche möglichen Risiken, Beschwerden oder Begleiterscheinungen sind mit Ihrer Teilnahme verbunden?",
    "Welcher mögliche Nutzen ergibt sich aus Ihrer Teilnahme an der Studie?",
    "Welche Rechte und Bedingungen sind mit der Teilnahme verbunden?",
    "Datenschutz",
    "1. Wer ist verantwortlich für die Datenverarbeitung und -speicherung?",
    "Verantwortliche Einrichtung",
    "2. An wen können Sie sich bei Fragen zur Studie oder zum Datenschutz wenden?",
    "Ansprechpartner zur Studie",
    "Datenschutzbeauftragter der Universitätsmedizin Rostock",
    "Zuständige Datenschutzaufsichtsbehörde",
    "3. Welche Daten von Ihnen benötigen wir für die Durchführung der Studie?",
    "4. Woher erhalten wir diese Daten?",
    "5. Zu welchen Zwecken werden Ihre Daten benötigt und wie werden sie geschützt?",
    "6. Wo und wie lange werden die Daten gespeichert?",
    "7. Wer erlangt Kenntnis von Ihren Daten? Werden Ihre Daten weitergegeben und veröffentlicht?",
    "8. Welche Datenschutzrechte haben Sie bei einer Teilnahme an der Studie?",
    "Widerrufsrecht",
    "Einwilligungserklärung",
    "zur Teilnahme an der Studie Sugar-Sugar Glukoseprognose-Studie",
    "und die damit verbundene Datenverarbeitung",
}

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

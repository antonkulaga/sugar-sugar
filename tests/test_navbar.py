from __future__ import annotations

from sugar_sugar.components.navbar import NavBar, get_navbar_back_href
from sugar_sugar.i18n import t


def test_navbar_contains_home_button_and_back(monkeypatch):
    current = "/prediction"
    navbar = NavBar(locale="en", current_page=current)
    children = navbar.children
    # back, home, about, contact, demo
    assert len(children) == 5

    back_btn, home_btn, about_btn, contact_btn, demo_btn = children

    # back button navigates to the correct previous page
    assert back_btn.href == get_navbar_back_href(current)
    back_label = t("ui.common.back", locale="en")
    assert back_label in back_btn.children

    # home button points to root
    assert home_btn.href == "/"
    assert home_btn.children == t("ui.common.home", locale="en")

    # secondary nav buttons
    assert about_btn.href == "/about"
    assert contact_btn.href == "/contact"
    assert demo_btn.href == "/demo"

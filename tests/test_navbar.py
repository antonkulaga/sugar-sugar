from __future__ import annotations

from sugar_sugar.components.navbar import NavBar
from sugar_sugar.i18n import t


def test_navbar_fomantic_menu_structure():
    """NavBar renders a Fomantic UI massive blue inverted tabular menu with correct items."""
    navbar = NavBar(locale="en", current_page="/prediction")
    assert "ui massive blue inverted tabular menu" in navbar.className

    children = navbar.children
    # left items: Game, The Study, Video instructions, Contact us + right menu div
    assert len(children) == 5
    game_item, study_item, video_item, contact_item, right_menu = children

    assert game_item.href == "/"
    assert t("ui.common.game", locale="en") == game_item.children

    assert study_item.href == "/about"
    assert t("ui.common.the_study", locale="en") == study_item.children

    assert video_item.href == "/demo"
    assert t("ui.common.video_instructions", locale="en") == video_item.children

    assert contact_item.href == "/contact"
    assert t("ui.common.contact_us", locale="en") == contact_item.children

    # right menu contains only 4 language flags
    assert "right menu" in right_menu.className
    assert len(right_menu.children) == 4


def test_navbar_game_always_visible():
    """Game item is always shown, including on landing page."""
    navbar = NavBar(locale="en", current_page="/")
    assert len(navbar.children) == 5
    game_item = navbar.children[0]
    assert game_item.href == "/"
    assert "active" in game_item.className


def test_navbar_game_active_on_game_flow_pages():
    """Game tab is active on all game-flow pages."""
    for page in ("/", "/consent-form", "/startup", "/prediction", "/ending", "/final"):
        navbar = NavBar(locale="en", current_page=page)
        game_item = navbar.children[0]
        assert "active" in game_item.className, f"Game not active on {page}"


def test_navbar_active_page_highlighted():
    navbar = NavBar(locale="en", current_page="/about")
    study_item = navbar.children[1]
    assert "active" in study_item.className

    game_item = navbar.children[0]
    assert "active" not in game_item.className


def test_navbar_active_language_flag():
    navbar = NavBar(locale="de", current_page="/")
    right_menu = navbar.children[-1]
    lang_items = right_menu.children
    de_item = lang_items[1]  # en, de, uk, ro
    assert "active" in de_item.className
    en_item = lang_items[0]
    assert "active" not in en_item.className


def test_navbar_language_flags_compact():
    """Language flag items use lang-item class for compact styling."""
    navbar = NavBar(locale="en", current_page="/")
    right_menu = navbar.children[-1]
    for flag_item in right_menu.children:
        assert "lang-item" in flag_item.className

from typing import Optional
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from sugar_sugar.i18n import t


class NavBar(html.Div):
    """Navigation bar component that appears at the top of all pages."""

    def __init__(self, *, locale: str = "en", current_page: str = "/") -> None:
        self._locale: str = locale
        self._current_page: str = current_page

        super().__init__(
            children=self._create_navbar(),
            style={
                "backgroundColor": "#1e88e5",
                "padding": "12px 20px",
                "boxShadow": "0 2px 4px rgba(0,0,0,0.1)",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "flex-start",
                "marginBottom": "20px",
            },
        )

    def _create_navbar(self) -> list:
        """Create the navbar content."""
        back_href = get_navbar_back_href(self._current_page)
        
        back_button = html.A(
            "← " + t("ui.common.back", locale=self._locale),
            id="navbar-back-button",
            href=back_href,
            className="ui small basic button",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
            },
        )

        home_button = html.A(
            t("ui.common.home", locale=self._locale),
            id="navbar-home-button",
            href="/",
            className="ui small basic button",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
                "marginLeft": "8px",
            },
        )

        about_button = html.A(
            t("ui.common.about", locale=self._locale),
            id="navbar-about-button",
            href="/about",
            className="ui small basic button",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
                "marginLeft": "8px",
            },
        )

        contact_button = html.A(
            t("ui.common.contact_us", locale=self._locale),
            id="navbar-contact-button",
            href="/contact",
            className="ui small basic button",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
                "marginLeft": "8px",
            },
        )

        demo_button = html.A(
            t("ui.common.demo", locale=self._locale),
            id="navbar-demo-button",
            href="/demo",
            className="ui small basic button",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
                "marginLeft": "8px",
            },
        )

        return [back_button, home_button, about_button, contact_button, demo_button]


def get_navbar_back_href(pathname: Optional[str]) -> str:
    """Determine where the back button should navigate to based on current page."""
    if not pathname:
        pathname = "/"

    # Navigation mapping: from page -> back to page
    back_map = {
        "/consent-form": "/",
        "/startup": "/",
        "/prediction": "/startup",
        "/ending": "/prediction",
        "/final": "/ending",
    }

    return back_map.get(pathname, "/")

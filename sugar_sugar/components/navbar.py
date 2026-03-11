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
                "justifyContent": "space-between",
                "marginBottom": "20px",
            },
        )

    def _create_navbar(self) -> list:
        """Create the navbar content."""
        back_href = get_navbar_back_href(self._current_page)
        
        back_button = dbc.Button(
            "← " + t("ui.common.back", locale=self._locale),
            id="navbar-back-button",
            href=back_href,
            external_link=True,
            color="light",
            size="sm",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
            },
        )

        home_button = dbc.Button(
            t("ui.common.home", locale=self._locale),
            id="navbar-home-button",
            href="/",
            external_link=True,
            color="light",
            size="sm",
            style={
                "fontWeight": "600",
                "fontSize": "14px",
                "marginLeft": "8px",
            },
        )

        # App title/logo
        title = html.Div(
            t("ui.common.app_title", locale=self._locale),
            style={
                "color": "white",
                "fontSize": "20px",
                "fontWeight": "800",
                "flex": "1",
                "textAlign": "center",
            },
        )

        # Empty spacer for alignment
        spacer = html.Div(style={"width": "80px"})

        return [back_button, home_button, title, spacer]


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

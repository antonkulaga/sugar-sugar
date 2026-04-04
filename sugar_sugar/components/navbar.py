from dash import html
from sugar_sugar.i18n import t


_GAME_PAGES = frozenset({"/", "/consent-form", "/startup", "/prediction", "/ending", "/final"})


class NavBar(html.Div):
    """Fomantic UI massive blue inverted tabular menu navbar.

    Left items:  Game | The Study | Video instructions | Contact us
    Right items: language flags
    """

    def __init__(self, *, locale: str = "en", current_page: str = "/") -> None:
        self._locale: str = locale
        self._current_page: str = current_page

        super().__init__(
            children=self._create_navbar(),
            className="ui massive blue inverted tabular menu",
            style={"borderRadius": "0", "marginBottom": "0", "borderBottom": "none"},
            disable_n_clicks=True,
        )

    def _active_cls(self, *pages: str) -> str:
        """Return 'active item' if current page matches, else 'item'."""
        return "active item" if self._current_page in pages else "item"

    def _create_navbar(self) -> list:
        left_items: list = [
            html.A(
                t("ui.common.game", locale=self._locale),
                href="/",
                className=self._active_cls(*_GAME_PAGES),
                disable_n_clicks=True,
            ),
            html.A(
                t("ui.common.the_study", locale=self._locale),
                href="/about",
                className=self._active_cls("/about"),
                disable_n_clicks=True,
            ),
            html.A(
                t("ui.common.faq", locale=self._locale),
                href="/faq",
                className=self._active_cls("/faq"),
                disable_n_clicks=True,
            ),
            html.A(
                t("ui.common.video_instructions", locale=self._locale),
                href="/demo",
                className=self._active_cls("/demo"),
                disable_n_clicks=True,
            ),
            html.A(
                t("ui.common.contact_us", locale=self._locale),
                href="/contact",
                className=self._active_cls("/contact"),
                disable_n_clicks=True,
            ),
        ]

        right_menu = html.Div(
            self._language_flags(),
            className="right menu",
            disable_n_clicks=True,
        )

        return left_items + [right_menu]

    def _language_flags(self) -> list:
        langs = [
            ("en", "/assets/flags/gb.svg", "EN"),
            ("de", "/assets/flags/de.svg", "DE"),
            ("uk", "/assets/flags/ua.svg", "UA"),
            ("ro", "/assets/flags/ro.svg", "RO"),
            ("ru", "/assets/flags/ru.svg", "RU"),
            ("zh", "/assets/flags/cn.svg", "ZH"),
            ("fr", "/assets/flags/fr.svg", "FR"),
            ("es", "/assets/flags/es.svg", "ES"),
        ]
        items: list = []
        for code, flag_src, label in langs:
            cls = "active item lang-item" if self._locale == code else "item lang-item"
            items.append(
                html.A(
                    [
                        html.Img(src=flag_src, className="lang-flag", disable_n_clicks=True),
                        html.Span(f" {label}", style={"marginLeft": "4px"}, disable_n_clicks=True),
                    ],
                    id=f"lang-{code}",
                    className=cls,
                    style={"cursor": "pointer"},
                )
            )
        return items

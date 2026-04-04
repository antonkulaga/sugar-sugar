## Project overview

This project is a Sugar-Sugar game where the user gets the glucose value for some timespan and has to predict by drawing the lines on the chart. He is given a sequence that he has to prolong. The aim of the study is to measure human accuracy of the glucose predictions.
The project is a DASH app, with app.py being main, while glucose, metrics, prediction and startup are dash components. I has default example csv file to play and debug with but provide an option to upload your own csv files from dexcom, libre and other CGM-s.
We use session storage to allow multiple users workin on the same app. Predictions are stored in polars dataframe, there is also a dataframe for current prediction window and scrolling positions.
When the user draws the line it interpolates the position to detect closes glucose and time value (time measurements are done every 5 minutes) and then updates the dataframe with the prediction values.

## Build and test commands

uv is used as the package manager for the project.
uv run start is used to run the dash app.
uv run chart is the fast dev shortcut: it starts Dash with data pre-loaded and routes straight to the prediction chart (bypasses landing, startup, and consent). Use this whenever the user asks to debug or test the chart in the browser. Only fall back to uv run start when the user explicitly needs the startup/landing/consent screens. uv run chart accepts --file, --points, --start, --unit, --locale, --host, --port options. Use --prefill to pre-fill the prediction region with noisy ground-truth values so the submit/ending/metrics flow can be tested without drawing (--noise controls the noise level, default 5%). Always prefer uv run chart --prefill over attempting browser automation for testing submit or ending pages.

## Known Dash pitfalls

### n_clicks corruption on static pages (issue #29)

In Dash 4 (also reproduced in Dash 3), every `html.*` component tracks `n_clicks` by default. Clicking anywhere on a page — text, background, wrapper divs, flex gaps — increments `n_clicks` on the clicked element. This triggers a React re-render that corrupts the component tree: children below the click target silently disappear from the DOM. No server-side callback fires; this is purely a client-side renderer bug.

**Symptoms:** On `/ending` or `/final`, clicking any non-button area causes metrics, buttons, and other sections to vanish. The outer container's padding changes and content is truncated.

**Root cause:** Dash's React wrapper re-renders the component when `n_clicks` changes. During reconciliation of complex static layouts, the renderer drops child components.

**Fix applied:** `disable_n_clicks=True` on every non-interactive element:
- Main layout: `page-content`, `navbar-container`
- `create_ending_layout`: outer wrapper, disclaimer, round info, units, graph section, chart container, metrics, buttons container, switch-format section
- `create_final_layout`: outer wrapper, disclaimer, rounds played, ranking, played formats, overall metrics, per-round metrics table wrapper, switch-format section, restart button container

**Rule for new pages:** When building layouts that are primarily display-only (no drawing/click interactions), add `disable_n_clicks=True` to all `html.Div` and similar wrapper elements. Only omit it on elements that need click tracking (buttons, links, interactive graphs).

**What did NOT work:** CSS `pointer-events: none` on containers, global JS click interceptors in `assets/` (broke the prediction chart), pathname guards on callbacks, making DataTables non-interactive.

## Code style guidelines

Always use type-hints. 
For file pathes prefer to use pathlib, for cli - typer, for dataframes - polars. 
We try to split logic into components and use functional style when possible, avoiding unneccesary mutability and duplication.
We use eliot logging library with with start_action(action_type=u"action_name") as action pattern to log results to logs folder. We use to_nice_file, to_nice_stdout from pycomfort logging to tell where to save files
Avoid excessive try-catch blocks

### Dash debug reloader caveat

Dash `debug=True` uses Werkzeug's auto-reloader, which forks a child process that re-imports the entire module. Any runtime mutations to `app.layout` are lost on reload. To pass configuration that must survive the fork (e.g. `uv run chart --prefill`), use environment variables read at module-level import time, not post-layout mutations.

### localStorage hydration race condition

`dcc.Store` with `storage_type='local'` hydrates **asynchronously** after the initial server render. Each store hydrates independently — there is no guaranteed order. A callback triggered by one store hydrating as `Input` may read other stores via `State` before they have hydrated, seeing the server-default value (`None` or whatever `data=` was in the layout) instead of the persisted value.

**Rule:** When a callback needs data from multiple localStorage-backed stores to make a correct decision (e.g. `restore_page_on_load` needs both `last-visited-page` and `user-info-store`), make **all** of them `Input` — not `State`. Use a one-shot memory flag (`page-restore-done`) to prevent the callback from acting more than once. If a required store hasn't hydrated yet (`data` is still `None`), `raise PreventUpdate` to wait for the next firing.

**Corollary — don't clobber stores on `/`:** Callbacks like `initialize_data_on_url_change` that write to `full-df` / `current-window-df` must **not** load fresh data when `pathname` is `/` or any non-prediction page. The URL-change callback fires before stores hydrate; overwriting them destroys the persisted session that the resume flow needs.

### Slider and component persistence

Interactive Dash components (sliders, dropdowns, inputs) that are destroyed and recreated on page navigation lose their value unless `persistence=True` and `persistence_type=STORAGE_TYPE` are set. The `time-slider` on the prediction page is recreated every time `create_prediction_layout` runs (e.g. on resume). Without persistence it mounts with the layout-default value, which triggers `handle_time_slider` and re-slices `current-window-df` at the wrong position.

**Rule:** Any interactive component whose value must survive a layout rebuild (page navigation, resume, language change) needs `persistence=True, persistence_type=STORAGE_TYPE`.

### resume-dialog-target must be cleared after dismissal

`render_resume_dialog` has `Input('interface-language', 'data')` so the dialog text updates when language changes. But `resume-dialog-target` is a memory store — if it is not set to `None` when the dialog is dismissed, any later `interface-language` change (e.g. clicking a flag on `/ending`) will re-render the stale dialog on top of the current page.

**Rule:** Every callback that dismisses the resume dialog (`handle_resume_continue`, `handle_resume_start_over`) must set `resume-dialog-target` to `None` in addition to clearing `resume-dialog-container`.

### Mobile viewport

The app forces a desktop-width layout viewport (`_DESKTOP_LAYOUT_VIEWPORT_CSS_PX = 1280`) via a `meta_tags` viewport entry on the `Dash()` constructor. This makes mobile browsers scale the page like "Request desktop site" instead of using `width=device-width`. Do not revert to `device-width`; the chart/drawing UI is unusable at phone-width layouts.

## Learned User Preferences

- Never attempt browser automation (drawing predictions, clicking through multi-step forms) with LLM agents — it fails; always use `uv run chart --prefill` instead
- Use `fuser -k PORT/tcp` to kill stray Dash processes on a busy port
- Keep `logs/*` with `!logs/.gitkeep` in `.gitignore` to preserve the directory in git while ignoring log files; `.cursor/` must be fully gitignored
- The UI uses Fomantic UI (Semantic UI fork) classes alongside Dash — prefix interactive classes with `ui` (e.g. `ui green button`)

## Browser automation tips (cursor-ide-browser MCP)

- Elements with `disable_n_clicks=True` (including language flags and navbar wrappers) do **not** appear as interactive refs in `browser_snapshot`. You cannot click them by ref.
- CSS-selector-based clicks (`browser_click` with `selector: "#some-id"`) also fail on elements with `disable_n_clicks=True` — the Dash attribute strips the React event handlers the browser tool relies on.
- **Workaround that works:** Use `browser_navigate` with a `javascript:void(...)` URL to programmatically click the element via the DOM: `javascript:void(document.getElementById('lang-de').click())`. This bypasses the missing React handlers and fires the Dash callback correctly.
- Coordinate-based clicks (`browser_click` with `coordinates`) fail when the element is outside the default viewport (1024 px wide). Use `browser_resize` first, or prefer the JS workaround above.
- `browser_screenshot` does not exist; the correct tool name is `browser_take_screenshot`.

## Learned Workspace Facts

- The app uses Fomantic UI CSS/JS loaded via `external_stylesheets` and `external_scripts` (jQuery is loaded first as a dependency)
- GitHub repo is GlucoseDAO/sugar-sugar; issues are tracked there
- `suppress_callback_exceptions=True` is set on the Dash app to allow callbacks referencing components not yet in the layout
- The navbar is a Fomantic UI `massive blue inverted tabular menu` (`NavBar` class in `sugar_sugar/components/navbar.py`). Left items: Game, The Study, Video instructions, Contact us. Right items: language flags. The active tab is highlighted via a CSS bottom-border rule.
- `STORAGE_TYPE` env var controls `dcc.Store` `storage_type` and input `persistence_type` across the app; defaults to `local` (localStorage persists across sessions)
- When using `dcc.Store` with `storage_type='local'`, the store hydrates from localStorage client-side **asynchronously** after initial render; use it as callback `Input` (not `State`) to react to hydration — see "localStorage hydration race condition" pitfall above
- A `last-visited-page` store + `restore_page_on_load` callback restores the user's last page when `STORAGE_TYPE=local`; a resume dialog (continue / start over) appears for returning users. Page flow: `/` → `/startup` → `/prediction` → `/ending` → `/final`. The callback uses `user-info-store` and `full-df` as Inputs (not State) to avoid the hydration race
- `initialize_data_on_url_change` must only load fresh data when `pathname == '/prediction'` and `full-df` is empty. For all other pathnames it returns `no_update` to avoid clobbering persisted stores during resume
- `dcc.Location` must NOT have a hardcoded `pathname="/"` — it overrides the actual browser URL and breaks direct navigation to `/about`, `/contact`, etc. Omit `pathname` so it reads from the browser.
- Dash clientside callbacks cannot use the same `dcc.Store` as both Input and Output — causes `dc[namespace][function_name] is not a function` JS error. Use a separate store or `State` instead.
- `uv run start --clean` clears all browser localStorage on first connect via `clean-storage-flag` store + clientside callback; "Start Over" in the resume dialog reuses the same `clean-storage-flag` mechanism
- `_STATEFUL_PAGES` (`/prediction`, `/ending`) skip full `page-content` re-renders on language change to preserve interactive/chart state. Each stateful page needs its own `update_*_text_on_language_change` callback that targets individual element IDs. `/final` is **not** stateful — it re-renders fully via `update_on_language_change`.
- When adding a new stateful page or translatable text to an existing one, every translatable element needs a stable `id` and a corresponding `Output` in the page's language-change callback. Otherwise the text stays in the old language.
- The prediction area is 12 points (1 hour at 5-min intervals); the game requires predictions drawn to the end of the hidden area before submit. `MAX_ROUNDS` is configurable via `.env` (defaults to 12).
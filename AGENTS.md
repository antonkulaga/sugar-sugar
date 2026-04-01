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

### Mobile viewport

The app forces a desktop-width layout viewport (`_DESKTOP_LAYOUT_VIEWPORT_CSS_PX = 1280`) via a `meta_tags` viewport entry on the `Dash()` constructor. This makes mobile browsers scale the page like "Request desktop site" instead of using `width=device-width`. Do not revert to `device-width`; the chart/drawing UI is unusable at phone-width layouts.

## Learned User Preferences

- Never attempt browser automation (drawing predictions, clicking through multi-step forms) with LLM agents — it fails; always use `uv run chart --prefill` instead
- Use `fuser -k PORT/tcp` to kill stray Dash processes on a busy port
- Keep `logs/*` with `!logs/.gitkeep` in `.gitignore` to preserve the directory in git while ignoring log files; `.cursor/` must be fully gitignored
- The UI uses Fomantic UI (Semantic UI fork) classes alongside Dash — prefix interactive classes with `ui` (e.g. `ui green button`)

## Learned Workspace Facts

- The app uses Fomantic UI CSS/JS loaded via `external_stylesheets` and `external_scripts` (jQuery is loaded first as a dependency)
- GitHub repo is GlucoseDAO/sugar-sugar; issues are tracked there
- `suppress_callback_exceptions=True` is set on the Dash app to allow callbacks referencing components not yet in the layout
- The navbar back-button uses `html.A` with `href`; the callback wired to `navbar-back-link` is effectively dead code (component id is `navbar-back-button`)
- The consent/landing page requires scrolling the participant text to the bottom before checkboxes become interactive (enforced by `dcc.Interval` polling)
- `STORAGE_TYPE` env var controls `dcc.Store` `storage_type` and input `persistence_type` across the app; defaults to `local` (localStorage persists across sessions)
- `dcc.Markdown` was replaced with server-side Python `markdown` lib + `html.Iframe(srcDoc=...)` in `static_markdown.py` to avoid React 18 async-markdown warnings
- When using `dcc.Store` with `storage_type='local'`, the store hydrates from localStorage client-side; use it as callback `Input` (not `State`) to react to hydration
- A `last-visited-page` store + `restore_page_on_load` callback restores the user's last page when `STORAGE_TYPE=local`; page flow: `/` → `/startup` → `/prediction` → `/ending` → `/final`
- `MAX_ROUNDS` is configurable via `.env` (defaults to 12)
- The app's CSS enforces `min-width: 1280px` on `html, body` as a fallback alongside the meta viewport `width=1280` for mobile desktop-view
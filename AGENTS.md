## Project overview

This project is a Sugar-Sugar game where the user gets the glucose value for some timespan and has to predict by drawing the lines on the chart. He is given a sequence that he has to prolong. The aim of the study is to measure human accuracy of the glucose predictions.
The project is a DASH app, with app.py being main, while glucose, metrics, prediction and startup are dash components. I has default example csv file to play and debug with but provide an option to upload your own csv files from dexcom, libre and other CGM-s.
We use session storage to allow multiple users workin on the same app. Predictions are stored in polars dataframe, there is also a dataframe for current prediction window and scrolling positions.
When the user draws the line it interpolates the position to detect closes glucose and time value (time measurements are done every 5 minutes) and then updates the dataframe with the prediction values.

## Build and test commands

uv is used as the package manager for the project.
uv run start is used to run the dash app.

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
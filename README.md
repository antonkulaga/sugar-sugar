# sugar-sugar
A fun game to test your glucose-predicting superpowers! 🎯

Ever wondered how good you are at predicting where your glucose levels are heading? sugar-sugar turns this into an engaging game where you test your glucose-spotting skills against real CGM data.

## How It Works

1. **Load Your Data**: Upload your own Dexcom or Libre CSV file, or use our example dataset (At the momemt we haven't yet fully tested the load your own data function-however the sample dataset is available and working)
2. **Make Predictions**: Click and draw on the glucose chart to predict future glucose values
3. **Compare Results**: Your predictions are compared against the actual glucose values from the file
4. **See Your Accuracy**: Get detailed metrics showing how close your predictions were to reality

The game shows you historical glucose data up to a certain point, then challenges you to predict what happens next. Since the file contains the actual "ground truth" values, we can precisely measure how accurate your human intuition is compared to what really happened.

Why did we create this? While fancy AI models are being built to predict glucose values, we realized nobody really knows how good humans are at this - especially experienced CGM users who've developed an instinct for their patterns. By playing sugar-sugar, you're not just having fun, you're also helping us understand:
- How accurate are humans at predicting glucose trends?
- What patterns do experienced CGM users notice that computers might miss?
- Could this help make better prediction tools in the future?

> 🎵 Fun fact: The name "sugar-sugar" was inspired by a scientific remake of The Archies' classic hit song ["Sugar, Sugar"](https://www.youtube.com/watch?v=jJvAL-iiLnQ) from 1969!

## Screenshots
![Game Interface](images/screenshot.png)
*sugar-sugar in action - try to predict where that line is going!*

## Setup

### Prerequisites
- Python 3.11 or higher
- UV (Python package manager)

### Installing UV
1. **Windows/macOS/Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Alternative method** (using pip):
```bash
pip install uv
```

3. **Using Homebrew** (macOS):
```bash
brew install uv
```

For detailed installation instructions, visit the [UV documentation](https://docs.astral.sh/uv/getting-started/installation/).

### Installation
1. Clone the repository:
```bash
git clone https://github.com/GlucoseDAO/sugar-sugar.git
cd sugar-sugar
```

2. Install dependencies using UV:
```bash
uv sync
```

3. Install development dependencies (optional):
```bash
uv sync --group dev
```

### Configuration
1. Copy the environment template and customize your settings:
```bash
cp .env.template .env
```

2. Edit `.env` to configure your server settings:
```bash
# Dash Application Configuration
DASH_HOST=127.0.0.1      # Host to run the server on
DASH_PORT=8050           # Port to run the server on
DASH_DEBUG=True          # Enable Dash debug mode
DEBUG_MODE=False         # Enable application debug features (test button)
```

### Running the Game
```bash
uv run start
```

You can also override configuration via command line:
```bash
# Run on a different host/port
uv run start --host 0.0.0.0 --port 3000

# Enable debug mode for development
uv run start --debug

# Combine options
uv run start --host 0.0.0.0 --port 3000 --debug
```

Note: Debug mode adds a "Just Test Me" button for quickly filling in the form during development.

### Quick Chart Debugging

To skip the landing/startup/consent pages and jump straight to the prediction chart:
```bash
uv run chart
```

This loads the example dataset, pre-fills test user info, and opens the prediction page immediately. You can also point it at your own CSV:
```bash
# Load an external Dexcom/Libre/Medtronic CSV
uv run chart --file /path/to/export.csv

# Pre-fill predictions with noisy ground truth (test submit/ending without drawing)
uv run chart --prefill
uv run chart --prefill --noise 0.10   # +/-10% noise

# Control the data window
uv run chart --points 48 --start 100

# Use mmol/L units and German locale
uv run chart --unit mmol/L --locale de

# Custom host/port
uv run chart --host 0.0.0.0 --port 3000
```

### Testing & Development Tips

#### Clearing localStorage

When `STORAGE_TYPE=local` (the default), all session data persists in the browser's `localStorage`. This is great for users but can get in the way during development — old state from a previous run may interfere with the feature you are testing. Use the `--clean` flag to wipe `localStorage` for every browser that connects:

```bash
uv run start --clean
```

While the server is running with `--clean`, every page load (including refreshes and new tabs) will call `localStorage.clear()` before anything else. Stop the server and restart without `--clean` to go back to normal persistence.

You can also clear storage manually in the browser via **DevTools → Application → Local Storage → Clear All**.

#### Testing the session resume dialog

The resume dialog only appears when `STORAGE_TYPE=local` and the browser already has a saved session from a previous visit. To test it end-to-end:

1. Start the app normally:
   ```bash
   uv run start
   ```
2. Walk through at least the landing and startup pages so that `localStorage` stores your progress (watch for `last-visited-page` in DevTools → Application → Local Storage).
3. Close the browser tab (do **not** stop the server).
4. Open `http://127.0.0.1:8050/` again — the resume dialog should appear with **Continue** / **Start Over** buttons and a warning about research data integrity.

For a faster loop, use `uv run chart --prefill` to get all the way to a submittable prediction in one step, submit the round, then close and reopen the tab.

#### Testing the full submit / ending / metrics flow

Drawing predictions by hand is slow. Use `--prefill` to populate the prediction region with noisy ground-truth values so you can immediately submit:

```bash
uv run chart --prefill                  # default ±5% noise
uv run chart --prefill --noise 0.10     # ±10% noise
```

This bypasses landing, startup, and consent, pre-fills user info, and auto-populates predictions — you land directly on the chart page ready to click **Submit**.

## KNOWN ISSUES:

- Currently only Dexcom and Libre 3 are supported. We will add support for other CGM devices soon.
- No scoring system and difficulty levels yet.
- Import your own data hasn't been fully tested

## FAQ

### Is this production-ready software?
This is an early-stage project meant for research and experimentation. The app now supports multiple users with session-based state management.

### Do you use my personal data?
Sugar-sugar supports **two modes**:

- **Play-only mode**: if you check **"I just want to play (do not store my CGM / gameplay data)"** on the landing page, the app will **not save study outputs** (no prediction statistics are written).
- **Study mode** (default): if you do *not* check play-only, the app may write **consent + study outputs** to CSV for research.

Notes:

- **Raw uploaded CGM files are used to run the game**. The app is designed to avoid keeping raw uploads permanently.
- In **study mode**, the app writes derived outputs (e.g. predictions vs ground truth + accuracy metrics) to `data/input/prediction_statistics.csv` and ranking info to `data/input/prediction_ranking.csv`.
- Consent choices are recorded to `data/input/consent_agreement.csv` (keyed by the same `study_id`).

### How accurate can glucose predictions be?
Glucose prediction is complex! Research shows that CGM data alone often isn't enough for highly accurate predictions. Other factors like physical activity, meals, insulin, and stress play crucial roles. For a deep dive into state-of-the-art machine learning approaches to glucose prediction, check out [GlucoBench](https://github.com/IrinaStatsLab/GlucoBench) ([paper](https://arxiv.org/abs/2410.05780)), which provides benchmarks and datasets for glucose prediction models.

### Can I contribute?
We welcome pull requests, bug reports, and feature suggestions through GitHub issues. Check out our contributing guidelines for more details.

### I have an idea for improvement!
Great! Feel free to:
- Open an issue to discuss your idea
- Submit a pull request with your changes
- Reach out to the contributors directly

## Contribution statement
- **Livia Zaharaia** (GlucoseDAO) - Core Developer
- **Anton Kulaga** (Institute for Biostatistics and Informatics in Medicine and Ageing Research) - Core Developer
- **Irina Gaynanova** (Department of Statistics and Department of Biostatistics, University of Michigan) - Scientific Advisor

## Technical Architecture

sugar-sugar is built with [Plotly Dash](https://dash.plotly.com/), creating an interactive web application for glucose prediction gaming. The app uses session-based state management to support multiple users and processes CGM data from Dexcom and Libre devices.

### Application Structure

```
sugar_sugar/
├── app.py                  # Main application and routing logic
├── config.py              # Application constants and configuration
├── data.py                 # Data loading and processing utilities
├── consent.py              # Consent CSV persistence utilities
└── components/             # Modular UI components
    ├── landing.py          # Landing + consent/choices page
    ├── startup.py          # User registration (demographics/medical history)
    ├── header.py           # Game controls and file upload
    ├── glucose.py          # Interactive glucose visualization
    ├── predictions.py      # Prediction data table
    ├── metrics.py          # Accuracy metrics display
    └── submit.py           # Game submission logic
    └── ending.py           # Results summary page
```

### Core Components and Their Roles

#### 1. **Application Core (`app.py`)**
- **Purpose**: Main application orchestration and routing
- **Key Features**:
  - Multi-page routing (landing → startup → prediction → ending)
  - Session storage management for user state
  - Component integration and callback coordination
  - Data format conversion between session storage and components

#### 2. **Landing Page (`landing.py`)**
- **Purpose**: First screen (study info + consent/choices)
- **Key Features**:
  - Play-only vs study mode selection
  - Optional checkboxes to receive results later / get updates
  - Consent choices saved to `data/input/consent_agreement.csv` (by `study_id`)

#### 3. **Startup Page (`startup.py`)**
- **Purpose**: User onboarding form (demographics / medical history)
- **Key Features**:
  - Comprehensive user information collection (demographics, medical history)
  - Form validation with required field indicators
  - Debug mode for development testing

#### 4. **Header Component (`header.py`)**
- **Purpose**: Game controls and data management
- **Key Features**:
  - CGM file upload (Dexcom/Libre CSV formats)
  - Time window position slider for data navigation
  - Points control for adjusting visible data range (24-48 points)
  - Game instructions and user guidance

#### 5. **Glucose Chart (`glucose.py`)**
- **Purpose**: Interactive glucose data visualization and prediction interface
- **Key Features**:
  - Displays historical glucose data from uploaded CSV files
  - Interactive prediction drawing via click-and-drag on the chart
  - Real-time glucose line plotting with color-coded safety ranges
  - Event markers for insulin, exercise, and carbohydrate events
  - Dynamic y-axis scaling based on data range
  - Session storage integration for state persistence

#### 6. **Prediction Table (`predictions.py`)**
- **Purpose**: Structured display comparing user predictions against ground truth
- **Key Features**:
  - Side-by-side comparison of predicted vs actual glucose values (from CSV)
  - Real-time table updates as predictions are drawn on the chart
  - Automatic interpolation between prediction points
  - Absolute and relative error calculations showing prediction accuracy
  - Time-indexed columns for easy temporal comparison

#### 7. **Metrics Component (`metrics.py`)**
- **Purpose**: Statistical accuracy measurement comparing predictions to ground truth
- **Key Features**:
  - Multiple accuracy metrics (MAE, RMSE, MAPE, R²) calculated against actual CSV values
  - Minimum 5 predictions required for statistical validity
  - Real-time calculation updates as more predictions are added
  - Detailed metric descriptions for user education about prediction quality

#### 8. **Submit Component (`submit.py`)**
- **Purpose**: Game completion and data export
- **Key Features**:
  - Prediction statistics export to CSV
  - User session data persistence
  - Unique session ID generation
  - Research data collection (anonymized)

#### 9. **Ending Page (`ending.py`)**
- **Purpose**: Results summary and game completion
- **Key Features**:
  - Complete prediction visualization
  - Final accuracy metrics display
  - Session summary with all predictions
  - Option to exit or restart

### Data Processing Layer (`data.py`)

- **CGM Format Detection**: Automatic detection of Dexcom vs Libre data formats
- **Data Standardization**: Conversion of different CGM formats to unified schema
- **Event Processing**: Extraction and categorization of diabetes management events
- **Time Series Handling**: Proper datetime parsing and chronological sorting

### State Management Architecture

The application uses Dash's `dcc.Store` components for state management. The storage backend is controlled by the `STORAGE_TYPE` environment variable:

| Value | Behaviour |
|-------|-----------|
| `local` (default) | Data persists in `localStorage` — survives browser restarts and tab closes. |
| `session` | Data persists in `sessionStorage` — cleared when the tab is closed. |
| `memory` | Data lives only in Dash's in-memory React state — cleared on any page refresh. |

- **Session Isolation**: Each browser gets its own storage namespace
- **Data Persistence**: User state maintained across page navigation
- **Component Communication**: Centralized state updates trigger component re-renders

#### Session Resume Dialog (`STORAGE_TYPE=local`)

When `STORAGE_TYPE=local`, user progress survives browser restarts. On the next visit the app detects the saved session and shows a **resume dialog** instead of silently redirecting:

1. A clientside callback persists the current page path into a `last-visited-page` store every time the user navigates.
2. On the very first page load, `restore_page_on_load` fires when localStorage hydrates `last-visited-page`. If the stored page is not `/` (landing), the callback computes the best restorable target (falling back to an earlier page when required data is missing) and writes it to `resume-dialog-target`.
3. `render_resume_dialog` renders a centered modal overlay showing the user's round progress and two buttons:
   - **Continue** — navigates to the stored target page; all session data is intact.
   - **Start Over** — resets every in-memory `dcc.Store` to its default value **and** triggers the `clean-storage-flag` clientside callback, which calls `localStorage.clear()` and self-resets. The user is taken back to the landing/consent page for a fresh start.
4. The dialog includes a warning discouraging users from restarting just because they are unhappy with their predictions, since that would skew research data.

The same `clean-storage-flag` mechanism is reused by the `--clean` CLI flag (`uv run start --clean`), which sets the flag at startup so every connecting browser gets its storage wiped.

> **Note for researchers:** The "Start Over" option is intentionally kept available (users must not feel trapped), but the warning makes it clear that restarting undermines research integrity. The dialog is only shown when a prior session actually exists — first-time visitors go straight to the landing page.

### Key Technical Features

- **Multi-CGM Support**: Handles both Dexcom G6 and Libre 3 data formats
- **Real-time Interactivity**: Immediate feedback as users make predictions
- **Responsive Design**: Bootstrap-based UI that works on various screen sizes
- **Play-only option**: You can play without writing study outputs
- **Research Integration**: In study mode, the app can write consent + derived prediction metrics for research

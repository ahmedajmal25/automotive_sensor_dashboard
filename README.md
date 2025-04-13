# Automotive Sensor Dashboard

A learning project to explore `pandas`, `numpy`, `matplotlib`, `seaborn`, and `plotly` with an engine health dataset.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run the dashboard:
   python3 -m src.main

4. Open http://127.0.0.1:8050/ in your browser.
   

Structure
data/: engine_data.csv
notebooks/: Jupyter exploration
src/: Source code
data/loader.py: Data loading
visualizations/dashboard.py: Dash app
visualizations/static_plots.py: Matplotlib/Seaborn plots
main.py: Entry point
tests/: Unit tests (TBD)


5. Install Dependencies
With `(venv)` active, install the required libraries:
pip install pandas numpy plotly dash matplotlib seaborn jupyter
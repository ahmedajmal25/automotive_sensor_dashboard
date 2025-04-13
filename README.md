# Automotive Sensor Dashboard

A learning project to explore `pandas`, `numpy`, `matplotlib`, `seaborn`, and `plotly` by building an interactive dashboard to visualize engine health data.

---

## Features

- **Interactive Dashboard**: Built with Dash to visualize engine sensor data.
- **Static Plots**: Includes Seaborn and Matplotlib visualizations.
- **Dynamic Visualizations**: Utilizes Plotly for interactive charts.
- **Data Preprocessing**: Standardized and cleaned dataset for analysis.

---

## Project Structure

```
automotive_sensor_dashboard/
├── data/                     # Contains the engine_data.csv dataset
├── notebooks/                # Jupyter notebooks for data exploration
├── src/                      # Source code for the project
│   ├── data/
│   │   └── loader.py         # Data loading and preprocessing
│   ├── visualizations/
│   │   ├── dashboard.py      # Dash app for interactive visualizations
│   │   └── static_plots.py   # Static plots using Matplotlib and Seaborn
│   └── main.py               # Entry point to run the dashboard
├── tests/                    # Unit tests (to be implemented)
└── README.md                 # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/automotive_sensor_dashboard2.git
cd automotive_sensor_dashboard2
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the dependencies:

```bash
pip install pandas numpy plotly dash matplotlib seaborn jupyter
```

### 4. Run the Dashboard

Run the main script to start the dashboard:

```bash
python3 -m src.main
```

### 5. Open the Dashboard

Open your browser and navigate to:

```
http://127.0.0.1:8050/
```

---

## Example Visualizations

### Pairplot (Seaborn)
Visualizes relationships between multiple sensor metrics.

### Violin Plot (Seaborn)
Shows the distribution of a selected sensor metric grouped by engine condition.

### Correlation Heatmap (Plotly)
Displays correlations between sensor metrics.

### 3D Scatter Plot (Plotly)
Interactive 3D visualization of engine RPM, coolant temperature, and fuel pressure.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Improvements

- Add unit tests for data loading and visualization functions.
- Enhance the dashboard with additional metrics and visualizations.
- Optimize performance for larger datasets.
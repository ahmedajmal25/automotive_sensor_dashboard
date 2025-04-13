# src/main.py
# Import functions to load data and create the dashboard
from src.data.loader import load_engine_data
from src.visualizations.dashboard import create_dashboard

def main():
    """
    Main function to load data, create the dashboard, and run the app.
    """
    # Load the engine health dataset
    df = load_engine_data()
    
    # Create the dashboard using the loaded dataset
    app = create_dashboard(df)
    
    # Run the dashboard app in debug mode
    app.run(debug=True)

# Entry point of the script
if __name__ == '__main__':
    main()
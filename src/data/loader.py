# src/data/loader.py
import pandas as pd
import os

def load_engine_data(file_path=None):
    """
    Load and preprocess the engine health dataset.
    
    Args:
        file_path (str, optional): Path to the CSV file. If not provided, a default path is used.
    
    Returns:
        pandas.DataFrame: Preprocessed dataset with standardized column names.
    """
    # If no file path is provided, use the default path in the 'data' folder
    if file_path is None:
        # Get the root directory of the project
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        # Construct the default file path
        file_path = os.path.join(project_root, 'data', 'engine_data.csv')
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Rename columns to have consistent and standardized names
    df.rename(columns={
        'Engine rpm': 'engine_rpm',
        'Lub oil pressure': 'lub_oil_pressure',
        'Fuel pressure': 'fuel_pressure',
        'Coolant pressure': 'coolant_pressure',
        'lub oil temp': 'lub_oil_temp',
        'Coolant temp': 'coolant_temp',
        'Engine Condition': 'engine_condition'
    }, inplace=True)
    
    # Return the preprocessed DataFrame
    return df
import pandas as pd
import os

def load_engine_data(file_path=None):
    """
    Load and preprocess the engine health dataset.
    
    Args:
        file_path (str, optional): Path to the CSV file. Defaults to 'data/engine_data.csv'.
    
    Returns:
        pandas.DataFrame: Preprocessed dataset with standardized column names.
    """
    if file_path is None:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        file_path = os.path.join(project_root, 'data', 'engine_data.csv')
    
    df = pd.read_csv(file_path)
    df.rename(columns={
        'Engine rpm': 'engine_rpm',
        'Lub oil pressure': 'lub_oil_pressure',
        'Fuel pressure': 'fuel_pressure',
        'Coolant pressure': 'coolant_pressure',
        'lub oil temp': 'lub_oil_temp',
        'Coolant temp': 'coolant_temp',
        'Engine Condition': 'engine_condition'
    }, inplace=True)
    
    return df
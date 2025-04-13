import matplotlib
matplotlib.use('Agg')  # Use non-interactive Agg backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from io import BytesIO
import base64

def save_plot_to_file_and_base64(buffer, output_path):
    """Helper function to save plot to file and return Base64 string."""
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

def create_pairplot(df, output_dir="static"):
    """Generates a pairplot for numeric columns, colored by engine condition."""
    os.makedirs(output_dir, exist_ok=True)
    pairplot = sns.pairplot(
        df, 
        hue='engine_condition', 
        vars=[
            'engine_rpm', 'lub_oil_pressure', 'fuel_pressure',
            'coolant_pressure', 'lub_oil_temp', 'coolant_temp'
        ]
    )
    pairplot.figure.suptitle("Pairplot of Engine Sensor Data", y=1.02)

    buffer = BytesIO()
    pairplot.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)

    output_path = os.path.join(output_dir, 'pairplot.png')
    return f"data:image/png;base64,{save_plot_to_file_and_base64(buffer, output_path)}"

def create_violinplot(df, column='engine_rpm', output_dir="static"):
    """Generates a violin plot for a specified column grouped by engine condition."""
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='engine_condition', y=column, data=df)
    plt.title(f"Violin Plot of {column.replace('_', ' ').title()} by Engine Condition")

    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)

    output_path = os.path.join(output_dir, f'violinplot_{column}.png')
    return f"data:image/png;base64,{save_plot_to_file_and_base64(buffer, output_path)}"
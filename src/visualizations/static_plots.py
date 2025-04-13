# src/visualizations/static_plots.py
import matplotlib
matplotlib.use('Agg')  # Use non-interactive Agg backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from io import BytesIO
import base64

def create_pairplot(df, output_dir="static"):
    """
    Create a pairplot for numeric columns, colored by engine condition.
    
    Args:
        df (pandas.DataFrame): The dataset containing the data.
        output_dir (str): Directory to save the plot image.
    
    Returns:
        str: Base64-encoded image string for embedding in Dash.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create the pairplot
    pairplot = sns.pairplot(
        df, 
        hue='engine_condition', 
        vars=[
            'engine_rpm', 'lub_oil_pressure', 'fuel_pressure',
            'coolant_pressure', 'lub_oil_temp', 'coolant_temp'
        ]
    )
    pairplot.fig.suptitle("Pairplot of Engine Sensor Data", y=1.02)

    # Save the plot to a buffer (for Dash) and to a file
    buffer = BytesIO()
    pairplot.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)  # Reset buffer position to the beginning

    # Convert the image to a Base64 string
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Save the plot as a file
    output_path = os.path.join(output_dir, 'pairplot.png')
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())

    # Close the buffer
    buffer.close()

    return f"data:image/png;base64,{img_base64}"

def create_violinplot(df, column='engine_rpm', output_dir="static"):
    """
    Create a violin plot for a specified column grouped by engine condition.
    
    Args:
        df (pandas.DataFrame): The dataset containing the data.
        column (str): The column to visualize.
        output_dir (str): Directory to save the plot image.
    
    Returns:
        str: Base64-encoded image string for embedding in Dash.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create the violin plot
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='engine_condition', y=column, data=df)
    plt.title(f"Violin Plot of {column.replace('_', ' ').title()} by Engine Condition")

    # Save the plot to a buffer (for Dash) and to a file
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)  # Reset buffer position to the beginning

    # Convert the image to a Base64 string
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Save the plot as a file
    output_path = os.path.join(output_dir, f'violinplot_{column}.png')
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())

    # Close the buffer
    buffer.close()

    return f"data:image/png;base64,{img_base64}"
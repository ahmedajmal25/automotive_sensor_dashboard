# src/visualizations/dashboard.py
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from src.visualizations.static_plots import create_pairplot, create_violinplot

def create_dashboard(df):
    """
    Create a Dash dashboard to visualize engine sensor data.
    
    Args:
        df (pandas.DataFrame): Preprocessed dataset.
    
    Returns:
        Dash: Configured Dash app.
    """
    # Initialize the Dash app
    app = Dash(__name__)

    # Generate static plots upfront
    pairplot_img = create_pairplot(df)  # Pairplot image (Base64-encoded)
    violinplot_rpm_img = create_violinplot(df, 'engine_rpm')  # Default violin plot image

    # Define the layout of the dashboard
    app.layout = html.Div([
        html.H1("Engine Health Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),
        
        # Dropdown for selecting sensor metrics
        html.Label("Select Sensor Metric for Boxplot and Violinplot:"),
        dcc.Dropdown(
            id='sensor-dropdown',
            options=[
                {'label': 'Engine RPM', 'value': 'engine_rpm'},
                {'label': 'Lub Oil Pressure', 'value': 'lub_oil_pressure'},
                {'label': 'Fuel Pressure', 'value': 'fuel_pressure'},
                {'label': 'Coolant Pressure', 'value': 'coolant_pressure'},
                {'label': 'Lub Oil Temp', 'value': 'lub_oil_temp'},
                {'label': 'Coolant Temp', 'value': 'coolant_temp'}
            ],
            value='engine_rpm',  # Default selection
            style={'width': '50%'}
        ),
        
        # Boxplot section
        html.H3("Boxplot (Plotly)", style={'textAlign': 'center'}),
        dcc.Graph(id='boxplot'),
        
        # Violin plot section
        html.H3("Violin Plot (Seaborn)", style={'textAlign': 'center'}),
        html.Img(id='violinplot', style={'width': '50%', 'display': 'block', 'margin': 'auto'}),
        
        # Correlation heatmap section
        html.H3("Correlation Heatmap (Plotly)", style={'textAlign': 'center'}),
        dcc.Graph(id='heatmap'),
        
        # Scatterplot section
        html.H3("Engine RPM vs Lub Oil Pressure (Plotly)", style={'textAlign': 'center'}),
        dcc.Graph(id='scatterplot'),
        
        # Pairplot section
        html.H3("Pairplot (Seaborn)", style={'textAlign': 'center'}),
        html.Img(src=pairplot_img, style={'width': '80%', 'display': 'block', 'margin': 'auto'}),
        
        # 3D scatter plot section
        html.H3("3D Scatter: RPM vs Coolant Temp vs Fuel Pressure (Plotly)", style={'textAlign': 'center'}),
        dcc.Graph(id='scatter3d')
    ])

    # Callback to update the boxplot based on the selected sensor
    @app.callback(
        Output('boxplot', 'figure'),
        Input('sensor-dropdown', 'value')
    )
    def update_boxplot(selected_sensor):
        # Create a boxplot using Plotly
        fig = px.box(
            df,
            y=selected_sensor,
            title=f"Distribution of {selected_sensor.replace('_', ' ').title()}",
            labels={selected_sensor: selected_sensor.replace('_', ' ').title()}
        )
        fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font=dict(size=12), showlegend=False)
        return fig

    # Callback to update the violin plot based on the selected sensor
    @app.callback(
        Output('violinplot', 'src'),
        Input('sensor-dropdown', 'value')
    )
    def update_violinplot(selected_sensor):
        # Generate a new violin plot image
        return create_violinplot(df, selected_sensor)

    # Callback to update the correlation heatmap
    @app.callback(
        Output('heatmap', 'figure'),
        Input('sensor-dropdown', 'value')
    )
    def update_heatmap(_):
        # Compute the correlation matrix and create a heatmap
        corr_matrix = df.corr()
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmin=-1,
            zmax=1,
            text=corr_matrix.values,
            texttemplate="%{text:.2f}",
            showscale=True
        ))
        fig.update_layout(
            title="Correlation Heatmap of Sensor Data",
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12),
            height=500
        )
        return fig

    # Callback to update the scatterplot
    @app.callback(
        Output('scatterplot', 'figure'),
        Input('sensor-dropdown', 'value')
    )
    def update_scatterplot(_):
        # Create a scatterplot of Engine RPM vs Lub Oil Pressure
        fig = px.scatter(
            df,
            x='engine_rpm',
            y='lub_oil_pressure',
            color='engine_condition',
            title="Engine RPM vs Lub Oil Pressure",
            labels={
                'engine_rpm': 'Engine RPM',
                'lub_oil_pressure': 'Lub Oil Pressure (Bar)',
                'engine_condition': 'Engine Condition'
            },
            opacity=0.6
        )
        fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', font=dict(size=12))
        return fig

    # Callback to update the 3D scatter plot
    @app.callback(
        Output('scatter3d', 'figure'),
        Input('sensor-dropdown', 'value')
    )
    def update_scatter3d(_):
        # Create a 3D scatter plot
        fig = px.scatter_3d(
            df,
            x='engine_rpm',
            y='coolant_temp',
            z='fuel_pressure',
            color='engine_condition',
            title='3D Scatter Plot: RPM vs Coolant Temp vs Fuel Pressure',
            labels={
                'engine_rpm': 'Engine RPM',
                'coolant_temp': 'Coolant Temperature (°C)',
                'fuel_pressure': 'Fuel Pressure (Bar)',
                'engine_condition': 'Engine Condition'
            },
            opacity=0.6
        )
        fig.update_layout(
            height=700,
            scene=dict(
                xaxis_title='Engine RPM',
                yaxis_title='Coolant Temp (°C)',
                zaxis_title='Fuel Pressure (Bar)'
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(size=12)
        )
        return fig

    return app
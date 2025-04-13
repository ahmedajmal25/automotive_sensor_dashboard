import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from src.visualizations.static_plots import create_pairplot, create_violinplot

def create_dashboard(df):
    """Create a Dash dashboard to visualize engine sensor data."""
    app = Dash(__name__)

    # Pre-generate static plots
    pairplot_img = create_pairplot(df)
    violinplot_rpm_img = create_violinplot(df, 'engine_rpm')

    # Dashboard layout
    app.layout = html.Div([
        html.H1("Engine Health Dashboard", style={'textAlign': 'center'}),
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
            value='engine_rpm',
            style={'width': '50%'}
        ),
        dcc.Graph(id='boxplot'),
        html.Img(id='violinplot', style={'width': '50%', 'display': 'block', 'margin': 'auto'}),
        dcc.Graph(id='heatmap'),
        dcc.Graph(id='scatterplot'),
        html.Img(src=pairplot_img, style={'width': '80%', 'display': 'block', 'margin': 'auto'}),
        dcc.Graph(id='scatter3d')
    ])

    # Callbacks
    @app.callback(Output('boxplot', 'figure'), Input('sensor-dropdown', 'value'))
    def update_boxplot(sensor):
        return px.box(
            df, y=sensor, title=f"Distribution of {sensor.replace('_', ' ').title()}",
            labels={sensor: sensor.replace('_', ' ').title()}
        ).update_layout(plot_bgcolor='white', paper_bgcolor='white', font=dict(size=12))

    @app.callback(Output('violinplot', 'src'), Input('sensor-dropdown', 'value'))
    def update_violinplot(sensor):
        return create_violinplot(df, sensor)

    @app.callback(Output('heatmap', 'figure'), Input('sensor-dropdown', 'value'))
    def update_heatmap(_):
        corr = df.corr()
        return go.Figure(data=go.Heatmap(
            z=corr.values, x=corr.columns, y=corr.columns, colorscale='RdBu', zmin=-1, zmax=1
        )).update_layout(
            title="Correlation Heatmap", plot_bgcolor='white', paper_bgcolor='white', font=dict(size=12), height=500
        )

    @app.callback(Output('scatterplot', 'figure'), Input('sensor-dropdown', 'value'))
    def update_scatterplot(_):
        return px.scatter(
            df, x='engine_rpm', y='lub_oil_pressure', color='engine_condition',
            title="Engine RPM vs Lub Oil Pressure",
            labels={'engine_rpm': 'Engine RPM', 'lub_oil_pressure': 'Lub Oil Pressure (Bar)'}
        ).update_layout(plot_bgcolor='white', paper_bgcolor='white', font=dict(size=12))

    @app.callback(Output('scatter3d', 'figure'), Input('sensor-dropdown', 'value'))
    def update_scatter3d(_):
        return px.scatter_3d(
            df, x='engine_rpm', y='coolant_temp', z='fuel_pressure', color='engine_condition',
            title='3D Scatter: RPM vs Coolant Temp vs Fuel Pressure',
            labels={
                'engine_rpm': 'Engine RPM', 'coolant_temp': 'Coolant Temp (°C)', 'fuel_pressure': 'Fuel Pressure (Bar)'
            }
        ).update_layout(
            height=700, scene=dict(
                xaxis_title='Engine RPM', yaxis_title='Coolant Temp (°C)', zaxis_title='Fuel Pressure (Bar)'
            ), plot_bgcolor='white', paper_bgcolor='white', font=dict(size=12)
        )

    return app
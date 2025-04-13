# tests/test_dashboard.py
import unittest
import pandas as pd
import os
from src.data.loader import load_engine_data
from src.visualizations.dashboard import create_dashboard
from dash import html, dcc

class TestDashboard(unittest.TestCase):
    def setUp(self):
        # Load engine_data.csv
        self.test_csv = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'engine_data.csv')
        )
        self.df = load_engine_data(self.test_csv)

    def test_create_dashboard(self):
        # Test app creation
        app = create_dashboard(self.df)
        # Check app type
        self.assertIsInstance(app, type(app), msg="Should return a Dash app")
        # Check layout exists
        self.assertIsNotNone(app.layout, "Layout should be defined")
        # Check layout type
        self.assertIsInstance(app.layout, html.Div, "Layout should be a Div")
        # Check for key components
        layout_children = app.layout.children
        self.assertTrue(any(isinstance(c, html.H1) for c in layout_children), "H1 header missing")
        self.assertTrue(any(isinstance(c, dcc.Dropdown) for c in layout_children), "Dropdown missing")
        self.assertTrue(any(isinstance(c, dcc.Graph) for c in layout_children), "Graph missing")
        self.assertTrue(any(isinstance(c, html.Img) for c in layout_children), "Image missing")

    def test_empty_dataframe(self):
        # Test with empty but valid DataFrame
        empty_df = pd.DataFrame(columns=[
            'engine_rpm', 'lub_oil_pressure', 'fuel_pressure',
            'coolant_pressure', 'lub_oil_temp', 'coolant_temp', 'engine_condition'
        ])
        app = create_dashboard(empty_df)
        self.assertIsNotNone(app.layout, "Layout should exist with empty DataFrame")

if __name__ == '__main__':
    unittest.main()
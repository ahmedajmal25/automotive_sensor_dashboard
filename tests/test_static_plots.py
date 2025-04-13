# tests/test_static_plots.py
import unittest
import pandas as pd
import os
from src.data.loader import load_engine_data
from src.visualizations.static_plots import create_pairplot, create_violinplot

class TestStaticPlots(unittest.TestCase):
    def setUp(self):
        # Load engine_data.csv
        self.test_csv = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'engine_data.csv')
        )
        self.df = load_engine_data(self.test_csv)
        self.output_dir = os.path.join(os.path.dirname(__file__), 'test_static')

    def test_create_pairplot(self):
        # Test pairplot generation
        result = create_pairplot(self.df, self.output_dir)
        # Check base64 format
        self.assertTrue(result.startswith('data:image/png;base64,'), "Pairplot should return base64 image")
        # Check output file exists
        output_path = os.path.join(self.output_dir, 'pairplot.png')
        self.assertTrue(os.path.exists(output_path), "Pairplot PNG should be saved")

    def test_create_violinplot(self):
        # Test violinplot generation
        result = create_violinplot(self.df, 'engine_rpm', self.output_dir)
        # Check base64 format
        self.assertTrue(result.startswith('data:image/png;base64,'), "Violinplot should return base64 image")
        # Check output file exists
        output_path = os.path.join(self.output_dir, 'violinplot_engine_rpm.png')
        self.assertTrue(os.path.exists(output_path), "Violinplot PNG should be saved")

    def test_invalid_column_violinplot(self):
        # Test with non-existent column
        with self.assertRaises(ValueError):
            create_violinplot(self.df, 'invalid_column', self.output_dir)

    def tearDown(self):
        # Clean up test_static directory
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

if __name__ == '__main__':
    unittest.main()
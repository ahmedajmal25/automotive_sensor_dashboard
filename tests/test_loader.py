# tests/test_loader.py
import unittest
import pandas as pd
import os
from src.data.loader import load_engine_data

class TestLoader(unittest.TestCase):
    def setUp(self):
        # Path to engine_data.csv in data/
        self.test_csv = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'data', 'engine_data.csv')
        )
        # Expected columns after renaming
        self.expected_columns = [
            'engine_rpm', 'lub_oil_pressure', 'fuel_pressure',
            'coolant_pressure', 'lub_oil_temp', 'coolant_temp', 'engine_condition'
        ]

    def test_load_engine_data(self):
        # Test loading engine_data.csv
        df = load_engine_data(self.test_csv)
        # Check type
        self.assertIsInstance(df, pd.DataFrame)
        # Check columns
        self.assertEqual(list(df.columns), self.expected_columns)
        # Check non-empty
        self.assertGreater(len(df), 0, "DataFrame should not be empty")
        # Check numeric columns
        for col in self.expected_columns[:-1]:  # Exclude engine_condition
            self.assertTrue(pd.api.types.is_numeric_dtype(df[col]), f"{col} should be numeric")

    def test_column_renaming(self):
        df = load_engine_data(self.test_csv)
        # Verify old column names are gone
        old_columns = [
            'Engine rpm', 'Lub oil pressure', 'Fuel pressure',
            'Coolant pressure', 'lub oil temp', 'Coolant temp', 'Engine Condition'
        ]
        for col in old_columns:
            self.assertNotIn(col, df.columns, f"Column {col} should be renamed")

    def test_file_not_found(self):
        # Test with non-existent file
        with self.assertRaises(FileNotFoundError):
            load_engine_data('non_existent.csv')

if __name__ == '__main__':
    unittest.main()
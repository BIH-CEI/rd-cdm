import unittest
import os
import csv
from src.parsing.create_rd_cdm_csv import create_final_rd_cdm_csv

class TestCreateRdCdmCsv(unittest.TestCase):
    """Tests for the function that creates both individual and combined CSV files."""

    def setUp(self):
        """Set up test environment."""
        self.version = "v2_0_0"
        self.output_dir = f"res/{self.version}/"
        self.code_systems_csv = os.path.join(
            self.output_dir, f"rd_cdm_codesystems_{self.version}.csv")
        self.data_elements_csv = os.path.join(
            self.output_dir, f"rd_cdm_data_elements_{self.version}.csv")
        self.value_sets_csv = os.path.join(
            self.output_dir, f"rd_cdm_value_sets_{self.version}.csv")
        self.combined_csv = os.path.join(
            self.output_dir, f"rd_cdm_{self.version}.csv")

    def test_create_final_rd_cdm_csv(self):
        """Test if the individual and combined CSV files are correctly created."""
        # Call the CSV creation function
        create_final_rd_cdm_csv(self.version)
        
        # Check if individual CSV files are created
        self.assertTrue(
            os.path.exists(self.code_systems_csv), 
            "Code systems CSV not created.")
        self.assertTrue(
            os.path.exists(self.data_elements_csv), 
            "Data elements CSV not created.")
        self.assertTrue(
            os.path.exists(self.value_sets_csv), 
            "Value sets CSV not created.")
        
        # Check if the

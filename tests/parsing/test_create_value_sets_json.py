import unittest
import os
import json
from src.parsing.create_value_sets_json import create_value_set_json

class TestCreateValueSetsJson(unittest.TestCase):
    """Tests for the function that creates value sets JSON."""

    def setUp(self):
        """Set up test environment."""
        self.version = "v2_0_0"
        self.output_file = f"res/{self.version}/rd_cdm_value_sets_{self.version}.json"
    
    def test_create_value_sets_json(self):
        """Test if the value sets JSON file is correctly created."""
        # Call the function to create the value sets JSON
        create_value_set_json(self.version)
        
        # Check if the file was created
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        
        # Open and load the created JSON file
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        
        # Assert that the data is a dictionary
        self.assertIsInstance(data, dict, "Output is not a dictionary")
        
        # Check if "valueSets" key is present in the JSON
        self.assertIn("valueSets", data, "'valueSets' not found in JSON")
        
        # Optional: Check if the version is correctly set in the JSON
        self.assertEqual(data.get("version"), self.version, "Version mismatch in JSON")

if __name__ == "__main__":
    unittest.main()

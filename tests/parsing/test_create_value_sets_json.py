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
        create_value_set_json(self.version)
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("valueSets", data)

    # def tearDown(self):
    #     """Clean up after tests."""
    #     if os.path.exists(self.output_file):
    #         os.remove(self.output_file)

if __name__ == "__main__":
    unittest.main()

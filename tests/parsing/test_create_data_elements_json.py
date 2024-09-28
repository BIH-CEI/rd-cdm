import unittest
import os
import json
from src.parsing.create_data_elements_json import create_data_elements_json

class TestCreateDataElementsJson(unittest.TestCase):
    """Tests for the function that creates data elements JSON."""

    def setUp(self):
        """Set up test environment."""
        self.version = "v2_0_0"
        self.output_file = f"res/{self.version}/rd_cdm_data_elements_{self.version}.json"
    
    def test_create_data_elements_json(self):
        """Test if the data elements JSON file is correctly created."""
        create_data_elements_json(self.version)
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("dataElements", data)

    # def tearDown(self):
    #     """Clean up after tests."""
    #     if os.path.exists(self.output_file):
    #         os.remove(self.output_file)
        for element in data["dataElements"]:
            self.assertIn("dataType", element)
            self.assertIsInstance(element["dataType"], str)

if __name__ == "__main__":
    unittest.main()


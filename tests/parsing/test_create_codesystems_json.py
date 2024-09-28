import unittest
import os
import json
from src.parsing.create_codesystems_json import create_codesystem_json

class TestCreateCodeSystemsJson(unittest.TestCase):
    """Tests for the function that creates code systems JSON."""

    def setUp(self):
        """Set up test environment."""
        self.version = "v2_0_0"
        self.output_file = f"res/{self.version}/rd_cdm_codesystems_{self.version}.json"
    
    def test_create_codesystem_json(self):
        """Test if the code systems JSON file is correctly created."""
        create_codesystem_json(self.version)
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("CodeSystems", data)

    # def tearDown(self):
    #     """Clean up after tests."""
    #     if os.path.exists(self.output_file):
    #         os.remove(self.output_file)

if __name__ == "__main__":
    unittest.main()

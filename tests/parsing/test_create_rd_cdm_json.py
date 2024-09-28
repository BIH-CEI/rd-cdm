import unittest
import os
import json
from src.parsing.create_rd_cdm_json import create_final_rd_cdm_json

class TestCreateRdCdmJson(unittest.TestCase):
    """Tests for the function that creates the final RD CDM JSON file."""

    def setUp(self):
        """Set up test environment."""
        self.version = "v2_0_0"
        self.output_file = f"res/{self.version}/rd_cdm_{self.version}.json"

    def test_create_final_rd_cdm_json(self):
        """Test if the final RD CDM JSON file is correctly created."""
        # Create the final RD CDM JSON
        result = create_final_rd_cdm_json(self.version)
        
        # Check if the file was created
        self.assertTrue(os.path.exists(self.output_file), "Output file not created")
        
        # Check if the function returned the combined JSON
        self.assertIsNotNone(result, "Final RD CDM creation failed.")
        
        # Additional test to validate JSON structure
        with open(self.output_file, 'r') as f:
            data = json.load(f)
        
        # Check for the expected keys in the final RD CDM JSON
        self.assertIn("metadata", data)
        
        # Update this check to look for 'codeSystems' at the top level instead of inside 'metadata'
        self.assertIn("codeSystems", data)  # 'codeSystems' is now at the top level
        
        self.assertIn("dataElements", data)
        self.assertIn("valueSets", data)


    # def tearDown(self):
    #     """Clean up after tests."""
    #     if os.path.exists(self.output_file):
    #         os.remove(self.output_file)

if __name__ == "__main__":
    unittest.main()

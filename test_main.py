import unittest
from main import generate_terraform, validate_variables

class TestTerraformWrapper(unittest.TestCase):
    def test_generate_terraform(self):
        result = generate_terraform()
        self.assertIn("resource \"aws_instance\" \"example\"", result)
    
    def test_validate_variables(self):
        valid_vars = validate_variables()
        self.assertTrue(valid_vars)

if __name__ == "__main__":
    unittest.main()

import unittest
from data_validation import validate_salary

class TestValidateSalary(unittest.TestCase):

    def test_valid_salary(self):
        self.assertTrue(validate_salary(50000))
        self.assertTrue(validate_salary(0))
        self.assertTrue(validate_salary(12345.67))

    def test_invalid_salary_negative(self):
        self.assertFalse(validate_salary(-100))
        self.assertFalse(validate_salary(-0.01))

    def test_invalid_salary_non_numeric(self):
        self.assertFalse(validate_salary("abc"))
        self.assertFalse(validate_salary(None))
        self.assertFalse(validate_salary(""))

    def test_invalid_salary_special_characters(self):
        self.assertFalse(validate_salary("$50000"))
        self.assertFalse(validate_salary("50,000"))

if __name__ == '__main__':
    unittest.main()
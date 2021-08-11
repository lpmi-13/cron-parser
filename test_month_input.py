import unittest
from month_input import month_validation
from error_messages import MONTH_ERROR


class Test_Month(unittest.TestCase):
    def test_input_error_word(self):
        input = "february"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_not_valid_number(self):
        input = "20"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_negative_number(self):
        input = "-5"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_correct_number(self):
        input = "2"
        result = month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_asterisk(self):
        input = "*"
        result = month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_forward_slash(self):
        input = "*/4"
        result = month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_dash(self):
        input = "2-6"
        result = month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_comma(self):
        input = "6,8"
        result = month_validation(input)
        self.assertEqual(result, input)

    def test_input_error_symbol_forward_slash(self):
        input = "*/35"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_symbol_dash_first_number(self):
        input = "15-18"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_symbol_dash_second_number(self):
        input = "2-40"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_impossible_range(self):
        input = "10-2"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_range_with_non_number(self):
        input = "3-november"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_symbol_comma_first_number(self):
        input = "20,12"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

    def test_input_error_symbol_comma_second_number(self):
        input = "2,40"
        result = month_validation(input)
        self.assertEqual(result, MONTH_ERROR)

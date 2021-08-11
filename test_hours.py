import unittest
from hours_input import hours_validation
from error_messages import HOURS_ERROR


class HoursInput(unittest.TestCase):
    def test_input_error_word(self):
        input = "ten"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_not_valid_number(self):
        input = "35"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_negative_number(self):
        input = "-10"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_correct_number(self):
        input = "5"
        result = hours_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_asterisk(self):
        input = "*"
        result = hours_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_forward_slash(self):
        input = "*/4"
        result = hours_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_dash(self):
        input = "6-8"
        result = hours_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_comma(self):
        input = "2,5"
        result = hours_validation(input)
        self.assertEqual(result, input)

    def test_input_error_impossible_range(self):
        input = "6-2"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_range_with_non_number(self):
        input = "2-k"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_symbol_forward_slash(self):
        input = "*/29"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_symbol_dash_first_number(self):
        input = "28-10"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_symbol_dash_second_number(self):
        input = "5-25"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_symbol_comma_first_number(self):
        input = "30,12"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

    def test_input_error_symbol_comma_second_number(self):
        input = "2,45"
        result = hours_validation(input)
        self.assertEqual(result, HOURS_ERROR)

import unittest
from minutes_input import minutes_validation
from error_messages import MINUTES_ERROR


class Test_Minutes(unittest.TestCase):
    def test_input_error_word(self):
        input = "seven"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_not_valid_number(self):
        input = "95"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_negative_number(self):
        input = "-2"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_correct_number(self):
        input = "10"
        result = minutes_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_asterisk(self):
        input = "*"
        result = minutes_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_forward_slash(self):
        input = "*/15"
        result = minutes_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_dash(self):
        input = "10-20"
        result = minutes_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_comma(self):
        input = "10,20"
        result = minutes_validation(input)
        self.assertEqual(result, input)

    def test_input_error_symbol_forward_slash(self):
        input = "*/100"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_symbol_dash_first_number(self):
        input = "888-889"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_symbol_dash_second_number(self):
        input = "10-999"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_impossible_range(self):
        input = "20-10"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_range_with_non_number(self):
        input = "35-forever"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_symbol_comma_first_number(self):
        input = "300,40"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

    def test_input_error_symbo_comma_second_number(self):
        input = "10,400"
        result = minutes_validation(input)
        self.assertEqual(result, MINUTES_ERROR)

import unittest
from error_messages import DAY_OF_MONTH_ERROR
from day_of_month_input import day_of_month_validation


class Test_Day_Of_Month(unittest.TestCase):
    def test_input_error_word_with_suffix(self):
        input = "15th"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_word(self):
        input = "fifteenth"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_negative_number(self):
        input = "-28"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_correct_number(self):
        input = "12"
        result = day_of_month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_asterisk(self):
        input = "*"
        result = day_of_month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_forward_slash(self):
        input = "*/3"
        result = day_of_month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_dash(self):
        input = "10-15"
        result = day_of_month_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_comma(self):
        input = "5,20"
        result = day_of_month_validation(input)
        self.assertEqual(result, input)

    def test_input_error_impossible_range(self):
        input = "10-2"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_range_with_non_number(self):
        input = "18-$"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_symbol_forward_slash(self):
        input = "*/55"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_symbol_dash_first_number(self):
        input = "18-5"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_symbol_dash_second_number(self):
        input = "8-34"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_symbol_comma_first_number(self):
        input = "50,5"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

    def test_input_error_symbol_comma_second_number(self):
        input = "5,50"
        result = day_of_month_validation(input)
        self.assertEqual(result, DAY_OF_MONTH_ERROR)

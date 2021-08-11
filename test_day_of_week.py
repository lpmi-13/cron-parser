import unittest
from error_messages import DAY_OF_WEEK_ERROR
from day_of_week_input import day_of_week_validation


class Test_Day_Of_Week(unittest.TestCase):
    def test_input_error_word(self):
        input = "saturday"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_negative_number(self):
        input = "-2"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_impossible_number(self):
        input = "9"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_correct_number(self):
        input = "2"
        result = day_of_week_validation(input)
        self.assertEqual(result, input)

    def test_input_currect_symbol_asterisk(self):
        input = "*"
        result = day_of_week_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_forward_slash(self):
        input = "*/2"
        result = day_of_week_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_dash(self):
        input = "2-4"
        result = day_of_week_validation(input)
        self.assertEqual(result, input)

    def test_input_correct_symbol_comma(self):
        input = "2,6"
        result = day_of_week_validation(input)
        self.assertEqual(result, input)

    def test_input_error_impossible_range(self):
        input = "5-1"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_range_with_non_number(self):
        input = "4-forever"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_both_refer_to_sunday(self):
        input = "0-7"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_symbol_forward_slash(self):
        input = "*/20"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_symbol_dash_first_number(self):
        input = "10-2"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_symbol_dash_second_number(self):
        input = "3-20"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_symbol_comma_first_number(self):
        input = "20,3"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_symbol_comma_second_number(self):
        input = "4,50"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

    def test_input_error_symbol_comma_both_sunday(self):
        input = "0,7"
        result = day_of_week_validation(input)
        self.assertEqual(result, DAY_OF_WEEK_ERROR)

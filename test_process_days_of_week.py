import unittest
from process_values import process_days_of_week


class Test_Days_Of_Week_Output(unittest.TestCase):
    def test_days_of_week_single_number(self):
        input = "3"
        result = process_days_of_week(input)
        self.assertEqual(result, input)

    def test_all_days_of_week(self):
        input = "*"
        result = process_days_of_week(input)
        self.assertEqual(result, [str(i) for i in range(0, 7)])

    def test_days_of_week_comma(self):
        input = "1,4"
        result = process_days_of_week(input)
        self.assertEqual(result, ["1", "4"])

    def test_days_of_week_dash(self):
        input = "2-5"
        result = process_days_of_week(input)
        self.assertEqual(result, [str(i) for i in range(2, 5)])

    def test_days_of_week_forward_slash(self):
        input = "*/2"
        result = process_days_of_week(input)
        self.assertEqual(result, [str(i) for i in range(0, 7, 2)])

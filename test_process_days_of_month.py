import unittest
from process_values import process_days_of_month


class Test_Days_Of_Month_Output(unittest.TestCase):
    def test_days_of_month_single_number(self):
        input = "27"
        result = process_days_of_month(input)
        self.assertEqual(result, input)

    def test_all_days_of_month(self):
        input = "*"
        result = process_days_of_month(input)
        self.assertEqual(result, [str(i) for i in range(1, 32)])

    def test_days_of_month_comma(self):
        input = "13,27"
        result = process_days_of_month(input)
        self.assertEqual(result, ["13", "27"])

    def test_days_of_month_dash(self):
        input = "1-25"
        result = process_days_of_month(input)
        self.assertEqual(result, [str(i) for i in range(1, 25)])

    def test_days_of_month_forward_slash(self):
        input = "*/8"
        result = process_days_of_month(input)
        self.assertEqual(result, [str(i) for i in range(1, 32, 8)])

import unittest
from process_values import process_hours


class Test_Hours_Output(unittest.TestCase):
    def test_hours_single_number(self):
        input = "2"
        result = process_hours(input)
        self.assertEqual(result, input)

    def test_all_hours(self):
        input = "*"
        result = process_hours(input)
        self.assertEqual(result, [str(i) for i in range(0, 24)])

    def test_hours_comma(self):
        input = "3,7"
        result = process_hours(input)
        self.assertEqual(result, ["3", "7"])

    def test_hours_dash(self):
        input = "10-20"
        result = process_hours(input)
        self.assertEqual(result, [str(i) for i in range(10, 20)])

    def test_hours_forward_slash(self):
        input = "*/6"
        result = process_hours(input)
        self.assertEqual(result, [str(i) for i in range(0, 24, 6)])

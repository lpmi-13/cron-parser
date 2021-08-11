import unittest
from process_values import process_minutes


class Test_Minute_Output(unittest.TestCase):
    def test_minutes_single_number(self):
        input = "42"
        result = process_minutes(input)
        self.assertEqual(result, input)

    def test_all_minutes(self):
        input = "*"
        result = process_minutes(input)
        self.assertEqual(result, [str(i) for i in range(0, 60)])

    def test_minutes_comma(self):
        input = "3,7"
        result = process_minutes(input)
        self.assertEqual(result, ["3", "7"])

    def test_minutes_dash(self):
        input = "10-30"
        result = process_minutes(input)
        self.assertEqual(result, [str(i) for i in range(10, 30)])

    def test_minutes_forward_slash(self):
        input = "*/20"
        result = process_minutes(input)
        self.assertEqual(result, [str(i) for i in range(0, 60, 20)])

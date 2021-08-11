import re
from error_messages import MONTH_ERROR

dash_pattern = re.compile(r"\d-\d")


def month_validation(input):
    """
    months go from 1 - 12, they aren't 0-indexed
    """
    if input == "*":
        return input
    elif "," in input:
        left_number_string, right_number_string = input.split(",")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return MONTH_ERROR
        if left_number >= right_number:
            return MONTH_ERROR
        elif left_number > 11 or right_number > 12:
            return MONTH_ERROR
        elif left_number >= 1 and right_number <= 12:
            return input
        else:
            return MONTH_ERROR
    # we don't want negative numbers to fall in this block
    elif "-" in input and dash_pattern.search(input):
        left_number_string, right_number_string = input.split("-")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return MONTH_ERROR
        if left_number >= right_number:
            return MONTH_ERROR
        elif left_number >= 1 and right_number <= 12:
            return input
        else:
            return MONTH_ERROR
    elif "/" in input:
        left_token, right_token_string = input.split("/")
        try:
            right_token = int(right_token_string)
        except:
            return MONTH_ERROR
        if left_token != "*" or right_token > 12:
            return MONTH_ERROR
        else:
            return input
    else:
        try:
            input_number = int(input)
            if 1 <= input_number <= 12:
                return input
            else:
                return MONTH_ERROR
        except:
            return MONTH_ERROR

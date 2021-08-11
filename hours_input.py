import re
from error_messages import HOURS_ERROR

dash_pattern = re.compile(r"\d-\d")


def hours_validation(input):
    """
    the okay values here are *, a number between 0 and 23, a comma separated value between 0 and 23, and a dash saparated value between 0 and 23.
    """
    if input == "*":
        return input
    elif "," in input:
        left_number_string, right_number_string = input.split(",")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return HOURS_ERROR
        if left_number >= right_number:
            return HOURS_ERROR
        elif left_number > 22 or right_number > 23:
            return HOURS_ERROR
        elif left_number >= 0 and right_number <= 23:
            return input
        else:
            return HOURS_ERROR
    # we don't want negative numbers to fall in this block
    elif "-" in input and dash_pattern.search(input):
        left_number_string, right_number_string = input.split("-")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return HOURS_ERROR
        if left_number >= right_number:
            return HOURS_ERROR
        elif left_number >= 0 and right_number <= 23:
            return input
        else:
            return HOURS_ERROR
    elif "/" in input:
        left_token, right_token_string = input.split("/")
        try:
            right_token = int(right_token_string)
        except:
            return HOURS_ERROR
        if left_token != "*" or right_token > 23:
            return HOURS_ERROR
        else:
            return input
    else:
        try:
            number_input = int(input)
            if 0 <= number_input <= 23:
                return input
            else:
                return HOURS_ERROR
        except:
            return HOURS_ERROR

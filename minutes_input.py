import re
from error_messages import MINUTES_ERROR

dash_pattern = re.compile(r"\d-\d")


def minutes_validation(input):
    if input == "*":
        return input
    elif "," in input:
        left_number_string, right_number_string = input.split(",")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return MINUTES_ERROR
        if left_number >= right_number:
            return MINUTES_ERROR
        elif left_number > 58 or right_number > 59:
            return MINUTES_ERROR
        elif left_number >= 0 and right_number <= 59:
            return input
        else:
            return MINUTES_ERROR
    # we don't want negative numbers to fall in this block
    elif "-" in input and dash_pattern.search(input):
        left_number_string, right_number_string = input.split("-")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return MINUTES_ERROR
        if left_number >= right_number:
            return MINUTES_ERROR
        elif left_number >= 0 and right_number <= 59:
            return input
        else:
            return MINUTES_ERROR
    elif "/" in input:
        left_token, right_token_string = input.split("/")
        try:
            right_token = int(right_token_string)
        except:
            return MINUTES_ERROR
        if left_token != "*" or right_token > 59:
            return MINUTES_ERROR
        else:
            return input
    else:
        try:
            number_input = int(input)
            if 0 <= number_input <= 59:
                return input
            else:
                return MINUTES_ERROR
        except:
            return MINUTES_ERROR

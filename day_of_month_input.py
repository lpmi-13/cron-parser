import re
from error_messages import DAY_OF_MONTH_ERROR

dash_pattern = re.compile(r"\d-\d")


def day_of_month_validation(input):
    """
    like months, these aren't zero indexed. So the range is 1-31
    """
    if input == "*":
        return input
    elif "," in input:
        left_number_string, right_number_string = input.split(",")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return DAY_OF_MONTH_ERROR
        if left_number >= right_number:
            return DAY_OF_MONTH_ERROR
        elif left_number > 30 or right_number > 31:
            return DAY_OF_MONTH_ERROR
        elif left_number >= 1 and right_number <= 31:
            return input
        else:
            return DAY_OF_MONTH_ERROR
    # we don't want negative numbers to fall in this block
    elif "-" in input and dash_pattern.search(input):
        left_number_string, right_number_string = input.split("-")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return DAY_OF_MONTH_ERROR
        if left_number >= right_number:
            return DAY_OF_MONTH_ERROR
        elif left_number >= 1 and right_number <= 31:
            return input
        else:
            return DAY_OF_MONTH_ERROR
    elif "/" in input:
        left_token, right_token_string = input.split("/")
        try:
            right_token = int(right_token_string)
        except:
            return DAY_OF_MONTH_ERROR
        if left_token != "*" or right_token > 31:
            return DAY_OF_MONTH_ERROR
        else:
            return input
    else:
        try:
            input_number = int(input)
            if 1 <= input_number <= 31:
                return input
            else:
                return DAY_OF_MONTH_ERROR
        except:
            return DAY_OF_MONTH_ERROR

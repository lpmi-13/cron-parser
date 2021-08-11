import re
from error_messages import DAY_OF_WEEK_ERROR

dash_pattern = re.compile(r"\d-\d")


def day_of_week_validation(input):
    """
    these are weird, since both 0 and 7 refer to Sunday
    """
    if input == "*":
        return input
    elif "," in input:
        left_number_string, right_number_string = input.split(",")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return DAY_OF_WEEK_ERROR
        if left_number >= right_number:
            return DAY_OF_WEEK_ERROR
        elif left_number > 6 or right_number > 7:
            return DAY_OF_WEEK_ERROR
        elif left_number == 0 and right_number == 7:
            return DAY_OF_WEEK_ERROR
        elif left_number >= 0 and right_number <= 7:
            return input
        else:
            return DAY_OF_WEEK_ERROR
    # we don't want negative numebrs to fall in this block
    elif "-" in input and dash_pattern.search(input):
        left_number_string, right_number_string = input.split("-")
        try:
            left_number = int(left_number_string)
            right_number = int(right_number_string)
        except:
            return DAY_OF_WEEK_ERROR
        if left_number >= right_number:
            return DAY_OF_WEEK_ERROR
        # this is for the special case that both 0 and 7 refer to sunday
        elif left_number == 0 and right_number == 7:
            return DAY_OF_WEEK_ERROR
        elif left_number >= 0 and right_number <= 7:
            return input
        else:
            return DAY_OF_WEEK_ERROR
    elif "/" in input:
        left_token, right_token_string = input.split("/")
        try:
            right_token = int(right_token_string)
        except:
            return DAY_OF_WEEK_ERROR
        if left_token != "*" or right_token > 7:
            return DAY_OF_WEEK_ERROR
        else:
            return input
    else:
        try:
            number_input = int(input)
            if 0 <= number_input <= 7:
                return input
            else:
                return DAY_OF_WEEK_ERROR
        except:
            return DAY_OF_WEEK_ERROR

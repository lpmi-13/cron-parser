TOTAL_MINUTES = 59
TOTAL_HOURS = 23
# this is imprecise, but probably fine for now
TOTAL_DAYS_OF_MONTH = 31
TOTAL_MONTHS = 12
# this is because 0 and 7 both mean 'Sunday', so we'll just skip 7
TOTAL_DAYS_OF_WEEK = 6


def process_minutes(input):
    if input == "*":
        return [str(i) for i in range(0, TOTAL_MINUTES + 1)]
    elif "," in input:
        left_number, right_number = input.split(",")
        return [left_number, right_number]
    elif "-" in input:
        left_number, right_number = input.split("-")
        return [str(i) for i in range(int(left_number), int(right_number))]
    elif "/" in input:
        interval = int(input.split("/")[1])
        return [str(i) for i in range(0, TOTAL_MINUTES + 1, interval)]
    else:
        return input


def process_hours(input):
    if input == "*":
        return [str(i) for i in range(0, TOTAL_HOURS + 1)]
    elif "," in input:
        left_number, right_number = input.split(",")
        return [left_number, right_number]
    elif "-" in input:
        left_number, right_number = input.split("-")
        return [str(i) for i in range(int(left_number), int(right_number))]
    elif "/" in input:
        interval = int(input.split("/")[1])
        return [str(i) for i in range(0, TOTAL_HOURS + 1, interval)]
    else:
        return input


def process_days_of_month(input):
    if input == "*":
        # this could be more sophisticated, probably
        return [str(i) for i in range(1, TOTAL_DAYS_OF_MONTH + 1)]
    elif "," in input:
        left_number, right_number = input.split(",")
        return [left_number, right_number]
    elif "-" in input:
        left_number, right_number = input.split("-")
        return [str(i) for i in range(int(left_number), int(right_number))]
    elif "/" in input:
        interval = int(input.split("/")[1])
        return [str(i) for i in range(1, TOTAL_DAYS_OF_MONTH + 1, interval)]
    else:
        return input


def process_months(input):
    if input == "*":
        return [str(i) for i in range(1, TOTAL_MONTHS + 1)]
    elif "," in input:
        left_number, right_number = input.split(",")
        return [left_number, right_number]
    elif "-" in input:
        left_number, right_number = input.split("-")
        return [str(i) for i in range(int(left_number), int(right_number))]
    elif "/" in input:
        interval = int(input.split("/")[1])
        return [str(i) for i in range(1, TOTAL_MONTHS + 1, interval)]
    else:
        return input


def process_days_of_week(input):
    if input == "*":
        return [str(i) for i in range(0, TOTAL_DAYS_OF_WEEK + 1)]
    elif "," in input:
        left_number, right_number = input.split(",")
        return [left_number, right_number]
    elif "-" in input:
        left_number, right_number = input.split("-")
        return [str(i) for i in range(int(left_number), int(right_number))]
    elif "/" in input:
        interval = int(input.split("/")[1])
        return [str(i) for i in range(0, TOTAL_DAYS_OF_WEEK + 1, interval)]
    else:
        return input

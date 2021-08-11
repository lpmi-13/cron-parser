import sys

from error_messages import INVALID_INPUT
from minutes_input import minutes_validation
from hours_input import hours_validation
from day_of_month_input import day_of_month_validation
from month_input import month_validation
from day_of_week_input import day_of_week_validation

from process_values import process_minutes
from process_values import process_hours
from process_values import process_days_of_month
from process_values import process_months
from process_values import process_days_of_week


def input_validation(input):
    parsed_input = input.split(" ")
    if len(parsed_input) != 6:
        print(INVALID_INPUT)
        return

    minutes = minutes_validation(parsed_input[0])
    hours = hours_validation(parsed_input[1])
    days_of_month = day_of_month_validation(parsed_input[2])
    month = month_validation(parsed_input[3])
    days_of_week = day_of_week_validation(parsed_input[4])
    command = parsed_input[5]

    minutes = ' '.join(process_minutes(minutes)) if isinstance(process_minutes(minutes), list) else minutes
    hours = ' '.join(process_hours(hours)) if isinstance(process_hours(hours), list) else hours
    days_of_month = ' '.join(process_days_of_month(days_of_month)) if isinstance(process_days_of_month(days_of_month), list) else days_of_month
    month = ' '.join(process_months(month)) if isinstance(process_months(month), list) else month
    days_of_week = ' '.join(process_days_of_week(days_of_week)) if isinstance(process_days_of_week(days_of_week), list) else days_of_week

    # this should be working with the f-string formatting, but isn't for some reason
    print(
        f"minute        {minutes:5}\n"
        f"hour          {hours:5}\n"
        f"day of month  {days_of_month:5}\n"
        f"month         {month:5}\n"
        f"day of week   {days_of_week:5}\n"
        f"command       {command:5}"
    )


if __name__ == "__main__":
    input_validation(sys.argv[1])

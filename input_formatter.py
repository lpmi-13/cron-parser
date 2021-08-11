import sys
from input_validation import input_validation


def process_input(input):
    result = input_validation(input)
    if "invalid" in result:
        print(result)
    else:
        print(result)


if __name__ == "__main__":
    process_input(sys.argv[1])

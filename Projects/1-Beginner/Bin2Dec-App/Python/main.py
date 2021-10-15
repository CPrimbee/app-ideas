from typing import List

__initialize__: bool = True


def main():
    global __initialize__
    while __initialize__:
        answer = input("Multiple inputs? (y, N) ").capitalize()
        answer = answer if answer != "" else "N"

        if answer != "Y" and answer != "N":
            __initialize__ = False
            print("Invalid option!")

        input_binary_number(answer)

        keep_going()


def input_binary_number(multiple: str):
    if multiple == "N":
        single_input()
    else:
        multiple_input()


def single_input():
    binary_number: bin = input("Input an 8 digits binary number: ")

    if valid_binary(binary_number):
        print_result(binary_number, convert_bin_2_dec(binary_number))


def multiple_input():
    binary_numbers: List[bin] = input("Input a list of 8 digits binary numbers, separated by comma(,): ").split(",")

    for binary_number in binary_numbers:
        binary_number = binary_number.replace(" ", "")

        if valid_binary(binary_number):
            print_result(binary_number, convert_bin_2_dec(binary_number))


def valid_binary(binary_number: bin) -> bool:
    if len(binary_number) > 8:
        print(f"Max input's length is 8! You entered an binary with {binary_number} digits")
        return False

    allowed_numbers: list = ['0', '1']
    for digit in binary_number:
        if digit not in allowed_numbers:
            print("Input isn't a binary number")
            return False

    return True


def convert_bin_2_dec(binary_number: bin) -> str:
    counter: int = 0
    decimal_number: int = 0
    len_binary_number: int = len(binary_number) - 1

    while counter <= len_binary_number:
        index = len_binary_number - counter

        if int(binary_number[counter]) == 1:
            decimal_number += 2 ** index

        counter += 1

    return str(decimal_number)


def print_result(binary_number: bin, decimal_number: str):
    print(f"Typed binary number is {binary_number}. Its decimal equivalent is {decimal_number}")


def keep_going():
    global __initialize__
    must_continue = input("Continue ? (Y/n) ").capitalize()
    must_continue = must_continue if must_continue != "" else "Y"

    if must_continue != "Y" and must_continue != "N":
        __initialize__ = False
        print('Invalid option!')

    if must_continue == "N":
        __initialize__ = False


main()

__initialize: bool = True


def main():
    while __initialize:
        binary_number: bin = input("Input an 8 digits binary number: ")

        if valid_binary(binary_number):
            print(f"Typed binary number is {binary_number}. "
                  f"Its relative decimal is {convert_bin_2_dec(binary_number)}")

        keep_going()


def valid_binary(binary_number: bin) -> bool:
    if len(binary_number) > 8:
        print(f"Max input's length is 8! You entered an binary with {binary_number} digits")
        return False

    not_allowed_numbers: list = ['2', '3', '4', '5', '6', '7', '8', '9']
    for not_allowed_number in not_allowed_numbers:
        if not_allowed_number in binary_number:
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


def keep_going():
    global __initialize
    must_continue = input("Continue ? (Y/n) ").capitalize()
    if must_continue != "Y" and must_continue != "N":
        __initialize = False
        print('Invalid option!')
    if must_continue == "N":
        __initialize = False


main()

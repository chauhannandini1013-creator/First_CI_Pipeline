"""Program 30: Convert decimal to binary without bin()."""


def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary
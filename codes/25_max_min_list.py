"""Program 25: Find maximum and minimum without max() and min()."""


def find_max_min(numbers):
    if not numbers:
        raise ValueError("List is empty")
    maximum = numbers[0]
    minimum = numbers[0]
    for n in numbers[1:]:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return (maximum, minimum)
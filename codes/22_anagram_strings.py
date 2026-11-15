"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    a = first.replace(" ", "").lower()
    b = second.replace(" ", "").lower()
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)
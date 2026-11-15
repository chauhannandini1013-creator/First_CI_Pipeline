"""Program 27: Rotate a list to the right by k positions."""


def rotate_list(items, k):
    if not items:
        return []
    k = k % len(items)  # handles k bigger than length and negative k
    if k == 0:
        return list(items)
    return items[-k:] + items[:-k]
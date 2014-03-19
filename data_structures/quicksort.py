from time import time
from random import randrange


def quicksort(li):
    """The quicksort algorithm. Naively makes the pivot the last value
    in the list.
    """
    if len(li) < 2:
        return li

    pivot = li.pop()

    first = []

    length = len(li)
    i = 0
    while i < length:
        if li[i] <= pivot:
            first.append(li.pop(i))
            length -= 1
        else:
            i += 1

    return quicksort(first) + [pivot] + quicksort(li)


if __name__ == '__main__':
    pass

from time import time
from random import randrange


def quicksort(li):
    """The quicksort algorithm. Naively makes the pivot the last value
    in the list.
    """
    if len(li) < 2:
        return li

    pivot = li.pop()

    greater = []

    length = len(li)
    i = 0
    while i < length:
        if li[i] > pivot:
            greater.append(li.pop(i))
            length -= 1
        else:
            i += 1

    return quicksort(li) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print """
The quicksort algorithm performs respectably on lists that are unordered.
On a completely random list with 1000 values:
"""

    quick_avg = 0
    native_avg = 0
    for i in range(50):
        li = [randrange(100000) for i in range(1000)]
        start = time()
        quicksort(li)
        end = time()
        quick_avg += (end - start) / 50
        start = time()
        sorted(li)
        end = time()
        native_avg += (end - start) / 50

    print """quicksort: %s (average of 50 attempts)""" % quick_avg
    print """Native sort: %s (average of 50 attempts)""" % native_avg

    print """
The best case performance for my specific implementation, which chooses
the rightmost element of the list as pivot, is a list that is already
sorted. On a list of sequential values 1000 items long:
"""

    avg = 0
    for i in range(50):
        li = [i for i in range(100)]
        start = time()
        quicksort(li)
        end = time()
        quick_avg += (end - start) / 50
        start = time()
        sorted(li)
        end = time()
        native_avg += (end - start) / 50

    print """quicksort: %s (average of 50 attempts)""" % quick_avg
    print """Native sort: %s (average of 50 attempts)""" % native_avg

    print """
The worst case for my implementation is then a list sorted in reverse
order, as this requires that every item in the list be moved. On a list
of 1000 values sorted in descending order:
"""

    avg = 0
    for i in range(50):
        li = [i for i in range(100, 0, -1)]
        start = time()
        quicksort(li)
        end = time()
        quick_avg += (end - start) / 50
        start = time()
        sorted(li)
        end = time()
        native_avg += (end - start) / 50

    print """quicksort: %s (average of 50 attempts)""" % quick_avg
    print """Native sort: %s (average of 50 attempts)""" % native_avg

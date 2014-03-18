from time import time
from random import randrange


def insertion_sort(li):
    """Sort a list in-place using the insertion sort algorithm."""
    i = 1
    while(i < len(li)):
        if li[i] < li[i - 1]:
            j = 0
            while(j < i):
                if li[i] <= li[j]:
                    break
                j += 1

            li.insert(j, li.pop(i))
        i += 1


if __name__ == '__main__':
    print """
Insertion sort works pretty well on small data sets. Sorting a list containing
10 random numbers with insertion_sort and Python's native sort:
"""
    avg = 0
    for i in range(50):
        li = [randrange(100) for i in range(10)]
        start = time()
        insertion_sort(li)
        end = time()
        avg += (end - start) / 50

    print "Insertion sort: %s (average of 50 attempts)" % avg

    avg = 0
    for i in range(50):
        li = [randrange(100) for i in range(10)]
        start = time()
        li.sort()
        end = time()
        avg += (end - start) / 50

    print "Native sort: %s (average of 50 attempts)" % avg

    print """
Insertion sort is also strong when sorting a list of inputs that is already
nearly sorted. Sorting a list containing 100 sequential values where two
values have been swapped with each other:
"""
    avg = 0
    for i in range(50):
        li = [i for i in range(100)]
        li[40], li[50] = li[50], li[40]
        start = time()
        insertion_sort(li)
        end = time()
        avg += (end - start) / 50

    print "Insertion sort: %s (average of 50 attempts)" % avg

    avg = 0
    for i in range(50):
        li = [i for i in range(100)]
        li[40], li[50] = li[50], li[40]
        start = time()
        li.sort()
        end = time()
        avg += (end - start) / 50

    print "Native sort: %s (average of 50 attempts)" % avg

    print """
Insertion sort does not do nearly as well when sorting long lists and/or
lists that contain values that are not nearly sorted. Sorting a list of
100 completely random numbers:
"""
    avg = 0
    for i in range(50):
        li = [randrange(0, 100000) for i in range(100)]
        start = time()
        insertion_sort(li)
        end = time()
        avg += (end - start) / 50

    print "Insertion sort: %s (average of 50 attempts)" % avg

    avg = 0
    for i in range(50):
        li = [randrange(0, 100000) for i in range(100)]
        start = time()
        li.sort()
        end = time()
        avg += (end - start) / 50

    print "Native sort: %s (average of 50 attempts)" % avg

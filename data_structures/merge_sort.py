from time import time
from random import randrange


def merge_sort(li):
    """Sort a list using the merge sort algorithm."""
    if len(li) < 2:
        return li
    else:
        one = merge_sort(li[: len(li) / 2])
        two = merge_sort(li[len(li) / 2:])

        for i in range(len(two)):
            for j in range(len(one)):
                if two[i] < one[j]:
                    one.insert(j, two[i])
                    break
            else:
                one.append(two[i])

        return one


if __name__ == '__main__':
    print """
The pure, unadulterated merge sort algorithm is O(n*log n) in the average
case and in the worst case. The average case is one in which the list has
no prior sorting, and so is completely or mostly unordered.
"""

    avg = 0
    for i in range(50):
        li = [randrange(100000) for i in range(100)]
        start = time()
        merge_sort(li)
        end = time()
        avg += (end - start) / 50

    print """On a completely random list with 100 values:
%s (average of 50 attempts)""" % avg

    print """
The worst case is the case in which the list is already sorted, as this
forces the merge operation to iterate completely over the list that is
being merged into in order to place each item that is being merged in (as
the items being merged in will each be greater than the entire contents
of the list being merged into).
"""

    avg = 0
    for i in range(50):
        li = [i for i in range(100)]
        start = time()
        merge_sort(li)
        end = time()
        avg += (end - start) / 50

    print """On a list with 100 values in sequential order:
%s (average of 50 attempts)""" % avg

    print """
The best case for the merge sort is the case in which the list is in reverse
order, as each merge of an item into a sublist in the merge operation
requires only one step - each item being merged in is less than the entire
contents of the list being merged into.
"""

    avg = 0
    for i in range(50):
        li = [i for i in range(99, -1, -1)]
        start = time()
        merge_sort(li)
        end = time()
        avg += (end - start) / 50

    print """On a list with 100 values in reverse-sequential order:
%s (average of 50 attempts)""" % avg

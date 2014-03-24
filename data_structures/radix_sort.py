from queue import Queue
from quicksort import quicksort
from random import randrange
from time import time


def radix_sort_int(inlist):
    """The radix sort algorithm, implemented for base-10 integers. (Other
    data types may cause exceptions or not behave as you expect).
    """
    li = inlist[:]

    base = 10
    divisor = base

    buckets = [Queue() for i in range(base)]

    digits = 1
    i = 0
    while i < digits:
        for num in li:
            buckets[(num % divisor) // (divisor / base)].queue(num)
            if i == 0 and len(str(num)) > digits:
                digits = len(str(num))

        li = []

        for bucket in buckets:
            while bucket.size():
                li.append(bucket.dequeue())

        divisor *= base
        i += 1

    return li


def radix_sort_str(instr):
    """The radix sort algorithm implemented for strings. Sorts lexico-
    graphically.
    """
    li = instr[:]

    length = 0
    for i in li:
        if len(i) > length:
            length = len(i)

    buckets = {}

    i = length - 1
    while i >= 0:
        for word in li:
            try:
                bucket = buckets.setdefault(word[i], Queue())
            except IndexError:
                bucket = buckets.setdefault('0', Queue())

            bucket.queue(word)

        li = []

        #quicksort is used here to get the buckets out in lexicographical
        #order because calling radix_sort_str again would result in an
        #infinite recursion.
        for key in quicksort(buckets.keys()):
            while buckets[key].size():
                li.append(buckets[key].dequeue())

        i -= 1

    return li


if __name__ == '__main__':
    print """
Radix sort's complexity is O(k * n), where n is the number of list items
to be sorted and k is the number of digits or characters in the longest
number or string being sorted. This makes radix sort remarkably fast on
lists of relatively short strings or small integers. Sorting a list of
1000 values between 0 and 99:
"""

    radix_avg = 0
    for i in range(50):
        li = [randrange(100) for i in range(1000)]
        start = time()
        radix_sort_int(li)
        end = time()
        radix_avg += (end - start) / 50

    print """Radix sort: %s (average of 50 attempts)""" % radix_avg

    print """
However, radix sort's complexity linearly worsens when the strings in the
list become long or the integers numbers begin to contain many digits.
Sorting a list of 1000 values between 1,000,000,000 and 1,999,999,999:
"""

    radix_avg = 0
    for i in range(50):
        li = [randrange(1000000000, 2000000000) for i in range(1000)]
        start = time()
        radix_sort_int(li)
        end = time()
        radix_avg += (end - start) / 50

    print """Radix sort: %s (average of 50 attempts)""" % radix_avg

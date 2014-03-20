from queue import Queue


def radix_sort(inlist):
    """The radix sort algorithm, implemented for base-10 integers. (Other
    data types may cause exceptions or not behave as you expect).
    """
    li = inlist[:]

    base = 10
    divisor = base

    buckets = []
    for i in range(base):
        buckets.append(Queue())

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

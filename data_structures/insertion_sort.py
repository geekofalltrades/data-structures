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
    li = [4, 3, 2, 1]
    print li
    insertion_sort(li)
    print li

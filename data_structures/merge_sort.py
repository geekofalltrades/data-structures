def merge_sort(li):
    """Sort a list using the merge sort algorithm."""
    if len(li) == 1:
        return li
    else:
        one = merge_sort(li[: len(li) / 2])
        two = merge_sort(li[len(li) / 2 + 1:])

        for i in len(two):
            for j in len(one):
                if two[i] < one[j]:
                    one.insert(j, two[i])
                    break

        return one

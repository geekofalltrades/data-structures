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
    pass

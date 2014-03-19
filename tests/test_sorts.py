from data_structures.insertion_sort import insertion_sort
from data_structures.merge_sort import merge_sort
from data_structures.quicksort import quicksort
import unittest
from random import randrange


class TestSorts(unittest.TestCase):
    """Test the various sorting algorithms against each other."""
    def test_insertion_sort_against_native(self):
        """Sort 100 randomly generated lists of numbers with insertion
        sort and assert that their output matches that of Python's
        built-in sort.
        """
        for i in range(100):
            li = [randrange(0, 1000000) for x in range(100)]
            expected = sorted(li)
            insertion_sort(li)
            self.assertEqual(expected, li)

    def test_merge_sort_against_native(self):
        """Sort 100 randomly generated lists of numbers with merge sort
        and assert that their output matches that of Python's built-in
        sort.
        """
        for i in range(100):
            li = [randrange(0, 1000000) for x in range(100)]
            expected = sorted(li)
            li = merge_sort(li)
            self.assertEqual(expected, li)

    def test_quicksort_against_native(self):
        """Sort 100 randomly generated lists of numbers with quicksort
        and assert that their output matches that of Python's built-in
        sort.
        """
        for i in range(100):
            li = [randrange(0, 1000000) for x in range(100)]
            expected = sorted(li)
            li = quicksort(li)
            self.assertEqual(expected, li)

    def test_insertion_sort_against_merge_sort(self):
        """Sort 100 randomly generated lists of numbers with insertion
        sort and with merge sort and assert that their outputs match.
        """
        for i in range(100):
            insertion = [randrange(0, 1000000) for x in range(100)]
            merge = insertion[:]
            insertion_sort(insertion)
            merge = merge_sort(merge)
            self.assertEqual(insertion, merge)

    def test_insertion_sort_against_quicksort(self):
        """Sort 100 randomly generated lists of numbers with quicksort
        sort and with merge sort and assert that their outputs match.
        """
        for i in range(100):
            insertion = [randrange(0, 1000000) for x in range(100)]
            quick = insertion[:]
            insertion_sort(insertion)
            quick = quicksort(quick)
            self.assertEqual(insertion, quick)

    def test_merge_sort_against_quicksort(self):
        """Sort 100 randomly generated lists of numbers with merge sort
        sort and with quicksort and assert that their outputs match.
        """
        for i in range(100):
            quick = [randrange(0, 1000000) for x in range(100)]
            merge = quick[:]
            quick = quicksort(quick)
            merge = merge_sort(merge)
            self.assertEqual(quick, merge)

if __name__ == '__main__':
    unittest.main()

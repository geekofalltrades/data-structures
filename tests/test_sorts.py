from data_structures.insertion_sort import insertion_sort
import unittest
from random import randrange


class TestInsertionSort(unittest.TestCase):
    """Test the insertion sort."""
    def test_insertion_sort(self):
        """Sort 1000 randomly generated lists of numbers and assure that
        their output matches that of Python's built-in sort.
        """
        for i in range(100):
            li = [randrange(0, 1000000) for x in range(1000)]
            expected = sorted(li)
            insertion_sort(li)
            self.assertEqual(expected, li)


if __name__ == '__main__':
    unittest.main()

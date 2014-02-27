import unittest
from make_month import make_month
from random import randrange
from calendar import monthrange, weekday


class TestMakeMonth(unittest.TestCase):
    """Test some of the make_month function's basic functionality."""

    def setUp(self):
        pass

    def test_correct_num_days(self):
        """Test whether make_month returns DayLookup objects that contain
        the correct number of days for the month they're intended to
        represent.
        """
        for month in xrange(1, 13):
            numdays = monthrange(2014, month)[1]
            test_month = make_month(2014, month)
            self.assertEqual(numdays, test_month.length)


class TestDayLookup(unittest.TestCase):
    """Test the DayLookup object's ability to find the correct day of
    the week for a given date.
    """

    def setUp(self):
        self.weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        self.string_arg = '2nd'
        self.out_of_range_arg = 34

    def test_100_random_dates(self):
        """Using a random number generator, generate 100 random year-
        month-day sets and verify that DayLookup objects are able to re-
        turn the correct day each time."""
        ct = 0
        for i in xrange(100):
            year = randrange(1970, 2021)
            month = randrange(1, 13)
            day = randrange(1, monthrange(year, month)[1] + 1)

            expected = self.weekdays[weekday(year, month, day)]
            test_month = make_month(year, month)
            got = test_month.day(day)
            self.assertEqual(expected, got, "Failed with \
                %s %s %s : %s != %s; passed %s of 100" % \
                (year, month, day, expected, got, ct))
            ct += 1

    def test_argue_with_non_int(self):
        """Test that day() raises the appropriate exception when given an
        argument that is not an int.
        """
        test_month = make_month(2014, 2)
        self.assertRaises(TypeError, test_month.day, self.string_arg)

    def test_argue_with_out_of_bounds_int(self):
        """Test that day() raises the appropriate exception when given an
        integer argument that falls outside its calendar month.
        """
        test_month = make_month(2014, 2)
        self.assertRaises(ValueError, test_month.day, self.out_of_range_arg)


if __name__ == '__main__':
    unittest.main()

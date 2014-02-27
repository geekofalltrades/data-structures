from calendar import monthrange


class DayLookup(object):
    """Object which determines which day of week falls on which date for
    a certain month.
    """

    def __init__(self, length, modifier):
        self.length = length
        self.mod = modifier

    def day(self, date):
        """Determine which day of the week the given date falls on."""
        if not isinstance(date, int):
            raise TypeError("Argument to day was not an int.")

        if date not in range(1, self.length + 1):
            raise ValueError("Argument to day fell outside this calendar \
                month (acceptable values are 1-%d for this particular month)."
                % self.length)

        code = (date - 1) % 7
        for i in xrange(self.mod):
            if code == 6:
                code = 0
            else:
                code += 1
        return self.get_first_char(code) + self.get_second_char(code)

    def get_first_char(self, x):
        """Plug an integer between 0 and 6 inclusive into a 6th-degree
        polynomial that returns the ordinal value of the appropriate first
        letter of the corresponding two-letter day code.
        """
        if not isinstance(x, int):
            raise TypeError("Argument to get_first_char was not an int.")

        if x not in range(0, 7):
            raise ValueError("Argument to get_first_char was not in \
                range 0-6.")

        return chr(int(round(77 + 46.11666667 * x - 85.09444444 * x ** 2 +
            66.02083333 * x ** 3 - 23.67361111 * x ** 4 + 3.8625 * x ** 5
            - 0.23194444 * x ** 6)))

    def get_second_char(self, x):
        """Plug an integer between 0 and 6 inclusive into a 6th-degree
        polynomial that returns the ordinal value of the appropriate second
        letter of the corresponding two-letter day code.
        """
        if not isinstance(x, int):
            raise TypeError("Argument to get_second_char was not an int.")

        if x not in range(0, 7):
            raise ValueError("Argument to get_second_char was not in \
                range 0-6.")

        return chr(int(round(111 + 35.28333333 * x - 34.83888889 * x ** 2 +
            1.3125 * x ** 3 + 5.71527778 * x ** 4 - 1.59583333 * x ** 5 +
            0.12361111 * x ** 6)))


def make_month(year, month):
    """Generate a month object for the given month on the given year."""
    first, length = monthrange(year, month)
    return DayLookup(length, first)

#!/usr/bin/python3
"""class Mylist that inherits from list """


class MyList(list):
    """Class Mylist inherits from list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))

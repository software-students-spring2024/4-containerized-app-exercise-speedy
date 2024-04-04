"""
file to test app
"""

# import pytest

from web_app.app import *


class Tests:
    """
    test app
    """

    def test_sanity_check(self):
        """
        Sanity check 1
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_sanity_check2(self):
        """
        Sanity check 1
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

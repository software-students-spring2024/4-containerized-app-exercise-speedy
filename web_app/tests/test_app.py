"""
file to test app
"""

# import pytest

from web_app.app import display, image_capture


class Tests:
    """
    test app
    """

    def test_display(self):
        """
        test display route
        """
        display()
        assert True, "Expected True!"

    def test_sanity_check2(self):
        """
        test image capture route
        """
        image_capture()
        assert True, "Expected True!"

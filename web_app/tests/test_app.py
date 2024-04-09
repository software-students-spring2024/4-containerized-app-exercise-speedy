""" Module for testing app.py. """

from web_app.app import app


class Tests:
    """Class for testing app.py"""

    def test_sanity_check(self):
        """Function sanity check."""
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_index(self):
        """Function testing index."""
        response = app.test_client().get("/")
        assert response.status_code == 200

    def test_display(self):
        """Function testing display."""
        response = app.test_client().get("/display")
        assert response.status_code == 200

    def test_upload_image(self):
        """Function testing upload image."""
        response = app.test_client().post("/upload_image", data={"image_data": "test"})
        # test if the response code starts with 3 (3xx codes are for redirection)
        first_digit = response.status_code // 100
        assert first_digit == 3

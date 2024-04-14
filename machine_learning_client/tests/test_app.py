"""
file to test app
"""

from machine_learning_client.app import app, get_emoji_from_image, generate_label


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

    def test_get_emoji_from_image(self):
        """
        Test get emoji from image
        """
        image_url = "./images/test_image1.png"
        emoji_output = get_emoji_from_image(image_url)
        assert emoji_output == "Thumb_Up", "Expected emoji output to be 'Thumb_Up'"

    def test_generate_label(self):
        """
        Test generate label
        """
        image_url = "./images/test_image1.png"
        label = generate_label(image_url)
        assert label == "Thumb_Up", "Expected emoji label to be 'Thumb_Up'"

    def test_process_image(self):
        """
        Test process image
        """
        response = app.test_client().post("/processImage", json={"test": "test"})
        assert response.status_code in (200, 400)

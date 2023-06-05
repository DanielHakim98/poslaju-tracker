import PL as poslaju
import unittest


class TestPL(unittest.TestCase):
    def test_valid_format(self):
        valid_tn = "PL771883212383"
        self.assertEqual(poslaju.formatPL(valid_tn), True, "Invalid tracking number")

    def test_tn_not_14(self):
        """Should be be exactly 14 characters long"""
        not_14_char = "PL77188321238"
        self.assertEqual(
            poslaju.formatPL(not_14_char),
            False,
            "Should be be exactly 14 characters long",
        )

    def test_startwith_invalid_char(self):
        """
        Should start with these code:
        ["EE", "EH", "EP", "ER", "EN", "EM", "PL"]
        """
        invalid_startwith = "FF77188321238"
        self.assertEqual(
            poslaju.formatPL(invalid_startwith),
            False,
            """Should start with these code: ["EE", "EH", "EP", "ER", "EN", "EM", "PL"]""",
        )


unittest.main()

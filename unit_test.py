import PL as poslaju
import unittest


class TestPL(unittest.TestCase):
    def test_valid_format(self):
        valid_tn = "PL77188321238"
        self.assertEqual(poslaju.formatPL(valid_tn), True, "Invalid tracking number")

    def test_tn_not_13(self):
        """Should be be more or equal 13 characters long"""
        not_13_char = "PL7718832123"
        self.assertEqual(
            poslaju.formatPL(not_13_char),
            False,
            "Should be be more or equal 13 characters long",
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

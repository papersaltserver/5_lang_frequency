import unittest
from lang_frequency import get_most_frequent_words


class LangFrequencyTests(unittest.TestCase):
    def test_most_frequetn_words(self):
        test_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
        "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
        "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore "
        "eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt " 
        "mollit anim id est laborum.")
        test_result_list = get_most_frequent_words(test_text)
        self.assertTrue(test_result_list[0] == "ut")


if __name__ == 'main':
    unittest.main()
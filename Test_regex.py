import unittest
import regex


class TestRegex(unittest.TestCase):

    def test_numbers_only(self):
        self.assertEqual(regex.numbers_only("123450"), True)
        self.assertEqual(regex.numbers_only("Ab345zij"), False)

    def test_words_only(self):
        self.assertEqual(regex.words_only("hello its me asmin"), ['hello', 'its', 'me', 'asmin'])
        self.assertEqual(regex.words_only("+123 1567 .^*90"), ['123', '1567', '90'])

    def test_alpha_numeric(self):
        self.assertEqual(regex.alpha_numeric("abbreviation of water is h2o :) "), ['a', 'b', 'b', 'r', 'e', 'v', 'i',
                                                                                   'a', 't', 'i', 'o',
                                                                                   'n', 'o', 'f', 'w',
                                                                                   'a', 't', 'e', 'r',
                                                                                   'i', 's', 'h', '2', 'o'])

    def test_email_valid(self):
        self.assertEqual(regex.email_valid("asmin@gmail.com"), True)
        self.assertEqual(regex.email_valid("asmin.rai7@com"), False)


if __name__ == '__main__':
    unittest.main()

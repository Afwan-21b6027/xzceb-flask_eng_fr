import unittest

from translator import english_to_french, french_to_english

class test_Translator(unittest.TestCase):
    # def test_englishToFrenchNull(self):
    #     self.assertEqual(english_to_french(None), None)
    
    # def test_frenchToEnglishNull(self):
    #     self.assertEqual(french_to_english(None), None)

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToErench(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
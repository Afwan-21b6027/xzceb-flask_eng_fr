import unittest

from translator import englishToFrench, frenchToEnglish

class test_Translator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(),null)

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(),null)

if __name__ == '__main__':
    unittest.main()
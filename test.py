import unittest

from anagram import *

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(anagram('dog', 'god'))

    def test_anagram_fail(self):
        self.assertFalse(anagram('dog', 'cat'))


if __name__ == '__main__':
    unittest.main()  

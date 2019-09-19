import unittest
from kangaroo import kangaroo

class TestKangaroo(unittest.TestCase):

    def test_true(self):
        self.assertTrue(kangaroo('0 3 4 2'))
        self.assertTrue(kangaroo('1 2 2 1'))

    def test_false(self):
        self.assertFalse(kangaroo('1 2 3 5'))
        self.assertFalse(kangaroo('0 10 20 10'))
        self.assertFalse(kangaroo('20 100 19 100'))

    def test_zero_division(self):
        self.assertTrue(kangaroo('0 3 0 3'))
        self.assertTrue(kangaroo('1 2 1 2'))


    def test_invalid_input(self):
        with self.assertRaises(Exception):
            kangaroo([])

        with self.assertRaises(Exception):
            self.assertRaises(kangaroo('lorem ipsum'))

        with self.assertRaises(Exception):
            self.assertRaises(kangaroo('3 5 6'))

if __name__ == '__main__':
    unittest.main()
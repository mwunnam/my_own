#!/usr/bin/python3

import unittest

class Mytest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'. isupper())
        self.assertFalse('foo'. isupper())

    def test_split(self):
        s = 'We are the world'
        self.assertEqual(s.split(), ['We', 'are', 'the', 'world'])
        #check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


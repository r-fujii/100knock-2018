#!/usr/bin/env python3
import unittest

class Test(unittest.TestCase):
    def testfunc_is_stopword(self):
            self.assertTrue(is_stopword('in'))
            self.assertFalse(is_stopword('play'))


with open('./work/stopwords_en.txt') as f:
    stopwords_en = [word.rstrip() for word in f]   

def is_stopword(word):
    return True if word in stopwords_en else False


if __name__ == '__main__':
    unittest.main()
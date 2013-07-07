#!/usr/bin/env python

import unittest
import sys 

sys.path.append('../model')

from word import *

class WordTestCase(unittest.TestCase):
	def setUp(self):
		self.testcases=[
			('Test', 'Act of verifying something works as expected', 1),
			('Python', 'A amphibious reptile; Awesome programming language', 2),
			('', '', 0)
		]

	def test_wordlist(self):
		for (word,meaning,count) in self.testcases[:1]:
			w=Word(word, meaning)
			self.assertTrue(w.word, word)
			self.assertTrue(len(w.meanings), count)
	def test_correcterror(self):
		word,meaning,count = self.testcases[2]
		self.assertRaises(WrongWordException, Word,word,meaning)


if __name__ == '__main__':
	unittest.main()

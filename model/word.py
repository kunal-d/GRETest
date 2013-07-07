#!/usr/bin/env python

MEANING_SPLITTER=";"


class WrongWordException(Exception):
	def __init__(self, value):
		self.value=value

	def __str__():
		self.value


class Word:

	def __init__(self,word,meanings):
		if not word or not meanings:
			raise WrongWordException("Blank word or meaning provided.") 
		self.word=word
		self.meanings=meanings.split(MEANING_SPLITTER)

	@property
	def word(self): self.word

	@property
	def meanings(self): self.meanings


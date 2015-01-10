#!/usr/bin/env python

import sys

sys.path.append('..')

from model.word import *
from model.WordFactory import *
import random


class question:
	def __init__(self, question, correct_answer, options):
		self.question=question
		self.correct_answer=correct_answer
		self.options=options

	def printMe(self):

		OPTION_FORMAT = "\t%d) %s"
		print("q. %s" % self.question)
		for (i, option) in enumerate(self.options):
			print(OPTION_FORMAT % (i+1,option.strip()))

	def check_answer(self, answer):
		return int(answer-1)==self.correct_answer


class Test:
	def __init__(self, question, words):
		self.question=question
		self.words=words

	def generate_questions(self):

		NO_OPTIONS=4

		selected_words = random.sample(self.words, self.question)
		questions=[]
		for selected_word in selected_words:
			options=[None]*NO_OPTIONS
			correct_answer = random.randint(0,NO_OPTIONS-1)
			options[correct_answer] = random.choice(selected_word.meanings)
			incorrect_options = [random.choice(word.meanings) for word in random.sample(self.words,NO_OPTIONS-1)]

			for (i,option) in enumerate(options):
				if not option:
					options[i]=incorrect_options.pop()

			ques=question(selected_word.word, correct_answer, options)
			questions.append(ques)
		return questions

#def get_word_list():
#	word_cache=[]
#	def get_and_load_cache():
#		if len(word_cache):
#			words = WordFactory().load_default_words()
#			word_cache = words
#		return word_cache
#	return get_and_load_cache()

def get_word_list():
	return WordFactory().load_default_words()

def main():
	words=get_word_list()
	t=Test(10, words)
	questions=t.generate_questions()
	right=0
	for q in questions:
		q.printMe()
		ans = input()
		if q.check_answer(ans):
			print("\nCorrect\n")
			right+=1
		else:
			print("\nCorrect answer is %s" % q.options[q.correct_answer])
	print("Test completed. Your score is %2.0f%%"% (right/10.0*100) )

if __name__=='__main__':
	main()

import os
import os.path
import re
from word import Word

"""
This class fetches the list of words from the predefined directories. Words from additional directories can also be requested.
It assumes the word list is a text file with extension .list
"""

DEFAULT_EXTENSION=set(['list'])
WORD_LIST_DIR = ['../list']


class WordFactory:

	@staticmethod
	def get_default_dirs():
		return WORD_LIST_DIR

	def __init__(self):
		self.pattern = re.compile("([\w\(\)]+)\s+(.*)")
	

	def load_default_words(self):
		words=[]
		for directory in WordFactory.get_default_dirs():
			words.extend(self.load_words(directory))
		return words

	def has_correct_extension(self, file):
		return file.split(".")[-1] in DEFAULT_EXTENSION

	def createWord(self, line):
		matcher = self.pattern.match(line)
		if matcher:
			matched = list(matcher.groups())
			print(matched)
			w=Word(matched[0], matched[-1])
			return w
		return None

	def load_words(self, directory):
		if not os.path.isdir(directory):
			raise Exception("Incorrect directory:%s" % directory)
		for file in os.listdir(directory):
			print(file)
			if self.has_correct_extension(file):
				with open(directory+os.path.sep+file, 'r') as open_file:
					return [self.createWord(line) for line in open_file]
		return []	
	
def main():
	w = WordFactory()
	for word in w.load_default_words():
		print(word)

if __name__=='__main__':
	main()

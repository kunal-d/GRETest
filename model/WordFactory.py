import os
import os.path
import re

class WordFactory:
    "
	This class fetches the list of words from the predefined directories. Words from additional directories can also be requested.
	It assumes the word list is a text file with extension .list
	"

	DEFAULT_EXTENSION=set(['list'])
	WORD_LIST_DIR = ['../list']

	@staticmethod
	def get_default_dirs():
		return WORD_LIST_DIR

	def __init__(self):
		self.pattern = re.compile("([\w\(\)]+)\s+(.*)")
	

	def load_default_words(self):
		words=[]
		for directory in get_default_dirs():
			words.extend(self.load_words(directory))
		return words

	def load_words(self, directory):
		if not os.path.isdir(directory):
			raise Exception("Incorrect directory:%s" % directory)
		for file in os.list(directory):
			if has_correct_extension(file):
				with open(directory+os.path.sep+file, 'r') as open_file:
					return (createWord(line) for line in open_file)	
	

	def has_correct_extension(file):
		return file.split(".")[-1] in __DEFAULT_EXTENSION

	def createWord(line):
		matcher = self.pattern.match(line)
		if matcher:
			w=Word(matcher.groups[1], matcher.groups[-1])
			return w
		return None

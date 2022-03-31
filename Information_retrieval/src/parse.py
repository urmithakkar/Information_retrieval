__author__ = 'Nick Hirakawa'

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stemmer = PorterStemmer()

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')


class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
		blobs = s.split('#')[1:]
		for x in blobs:
			text = x.split()
			docid = text.pop(0)
			self.corpus[docid] = text

	def get_corpus(self):
		return self.corpus


class Query:

	def __init__(self, input_query):
		self.query = input_query
		self.queries = []

	#def parse(self):
		#with open(self.filename) as f:
		#	lines = ''.join(f.readlines())
		#self.queries = self.query.split()

	def get_queries(self):
		#self.queries = self.query.split()
		self.queries = tokenizer.tokenize(self.query)            #tokenizing each document
		sw = stopwords.words('english')
		self.queries = [stemmer.stem(token) for token in self.queries if token not in sw]
		return self.queries


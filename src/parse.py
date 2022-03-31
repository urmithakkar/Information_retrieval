__author__ = 'Nick Hirakawa'

import re


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
		self.queries = self.query.split()
		return self.queries


class ListElement(object):
	def __init__(self, itemsList, ordered=False):
		self.itemsList = itemsList
		self.ordered = ordered

	def __str__(self):
		if self.ordered:
			tag = 'ol'
		else:
			tag = 'ul'

		return '<' + tag + '>\n' + '\n'.join([('\t<li>' + x + '</li>') for x in self.itemsList]) + '\n</' + tag + '>'


class ParagraphElement(object):
	def __init__(self, text):
		self.text = text

	def __str__(self):
		return '<p>' + self.text + '</p>'

class HeaderElement(object):
	def __init__(self, text, level):
		self.text = text
		self.level = level

	def __str__(self):
		return '<h' + str(self.level) + '>' + self.text + '</h' + str(self.level) + '>'

class BlockQuoteElement(object):
	def __init__(self, subElements):
		self.subElements = subElements

	def __str__(self):
		return '<blockquote>\n' + '\n'.join(['\t' + str(x) for x in self.subElements]) + '\n</blockquote>'

class PreformattedCodeElement(object):
	def __init__(self, contents):
		self.contents = contents

	def __str__(self):
		return '<pre><code>' + self.contents + '</code></pre>'
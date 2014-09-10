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
from helpers import consistsEntirelyOf, isUnderlineForHeader

import re

class ElementType(object): # Simple enum class
	paragraph = 0

	header1 = 1
	header2 = 2
	header3 = 3
	header4 = 4
	header5 = 5
	header6 = 6

	blockquote = 7

	orderedListItem = 8
	unorderedListItem = 9

	orderedList = 10
	unorderedList = 11

	code = 12
	emphases = 13
	links = 14
	images = 15


class MarkupElement(object):
	def __init__(self, elementType=None, lineString=None, lineNumber=None):
		self.type = elementType
		self.lineString = lineString
		self.lineNumber = lineNumber
		self.text = None

	def setText(self, string):
		tempText = string

		# ---------------- First pass: ** or __ -> strong

		splitString = [el for el in re.split(r'\*\*|__', tempText) if el != '']

		tempText = ''

		i = 0
		while i + 2 < len(splitString):
			tempText += splitString[i] + '<strong>' + splitString[i+1] + '</strong>'

			i += 2

		tempText += splitString[-1]

		# ---------------- Second pass: * or _ -> em

		splitString = [el for el in re.split(r'\*|_', tempText) if el != '']

		tempText = ''

		i = 0
		while i + 2 < len(splitString):
			tempText += splitString[i] + '<em>' + splitString[i+1] + '</em>'

			i += 2

		tempText += splitString[-1]

		# ---------------- Third pass: links

		linkLocation = tempText.find('](')
		while linkLocation != -1:
			reverseIndex = linkLocation
			while reverseIndex > 0:
				if tempText[reverseIndex] == '[':
					linkText = tempText[reverseIndex+1:linkLocation]
					break

				reverseIndex -= 1

			forwardIndex = linkLocation
			while forwardIndex < len(tempText):
				if tempText[forwardIndex] == ')':
					linkAddr = tempText[linkLocation+2:forwardIndex]
					break
				
				forwardIndex += 1

			tempText = tempText[:reverseIndex] + '<a href="' + linkAddr + '">' + linkText + '</a>' + tempText[forwardIndex+1:]
			
			linkLocation = tempText.find('](')



		# --------------- Done, assign it

		self.text = tempText

	def __str__(self):
		if self.type == None:
			return ''

		tag = ''

		if self.type == ElementType.paragraph:
			tag = 'p'

		elif self.type == ElementType.header1:
			tag = 'h1'
		elif self.type == ElementType.header2:
			tag = 'h2'
		elif self.type == ElementType.header3:
			tag = 'h3'
		elif self.type == ElementType.header4:
			tag = 'h4'
		elif self.type == ElementType.header5:
			tag = 'h5'
		elif self.type == ElementType.header6:
			tag = 'h6'

		elif self.type == ElementType.blockquote:
			tag = 'blockquote'

		elif self.type == ElementType.unorderedList:
			tag = 'ul'
		elif self.type == ElementType.orderedList:
			tag = 'ol'

		return '<' + tag + '>' + str(self.text) + '</' + tag + '>'

class MarkdownParser(object):
	def __init__(self):
		self.elements = []

	def identify(self, lineString):
		if lineString == '':
			identifiedType = None

		elif lineString.startswith('######'):
			identifiedType = ElementType.header6
		elif lineString.startswith('#####'):
			identifiedType = ElementType.header5
		elif lineString.startswith('####'):
			identifiedType = ElementType.header4
		elif lineString.startswith('###'):
			identifiedType = ElementType.header3
		elif lineString.startswith('##'):
			identifiedType = ElementType.header2
		elif lineString.startswith('#'):
			identifiedType = ElementType.header1

		elif lineString.startswith('>'):
			identifiedType = ElementType.blockquote

		elif lineString.startswith('+'):
			identifiedType = ElementType.unorderedListItem

		elif re.match(r'[0-9]\.', lineString):
			identifiedType = ElementType.orderedListItem

		else:
			identifiedType = ElementType.paragraph

		return identifiedType


	def handle(self, lineType, lineIndex):
		line = self.lines[lineIndex]

		newElement = MarkupElement(elementType=lineType)

		if (lineType == ElementType.header1 or 
		   lineType == ElementType.header2 or
		   lineType == ElementType.header3 or
		   lineType == ElementType.header4 or
		   lineType == ElementType.header5 or
		   lineType == ElementType.header6):
			newElement.setText(line.lstrip('#').lstrip())

		elif lineType == ElementType.paragraph:
			# Test if "paragraph" is actually a header
			if lineIndex < len(self.lines) - 1 and isUnderlineForHeader(self.lines[lineIndex + 1]):
				if (self.lines[lineIndex + 1][0] == '='):
					newElement.type = ElementType.header1
				elif (self.lines[lineIndex + 1][0] == '-'):
					newElement.type = ElementType.header2

				newElement.setText(line)
				lineIndex += 1

			# It's actually a paragraph
			else:
				string = line
				while (lineIndex + 1 < len(self.lines)) and (self.identify(self.lines[lineIndex + 1]) == ElementType.paragraph):
					string += ('\n' + self.lines[lineIndex + 1])
					lineIndex += 1

				newElement.setText(string)

		elif lineType == ElementType.unorderedListItem:
			newElement.type = ElementType.unorderedList
			string = '<li>' + line.lstrip('+').lstrip() + '</li>'

			while (lineIndex + 1 < len(self.lines)) and (self.identify(self.lines[lineIndex + 1]) == ElementType.unorderedListItem):
				string += ('\n' + '<li>' + self.lines[lineIndex + 1].lstrip('+').lstrip() + '</li>')
				lineIndex += 1

			newElement.setText(string)

		elif lineType == ElementType.orderedListItem:
			newElement.type = ElementType.orderedList
			string = '<li>' + '.'.join(line.split('.')[1:]).lstrip() + '</li>'

			while (lineIndex + 1 < len(self.lines)) and (self.identify(self.lines[lineIndex + 1]) == ElementType.orderedListItem):
				string += ('\n' + '<li>' + '.'.join(self.lines[lineIndex + 1].split('.')[1:]).lstrip() + '</li>')
				lineIndex += 1

			newElement.setText(string)

		elif lineType == ElementType.blockquote:
			newElement.type = ElementType.blockquote
			string = ''

			tempString = line.lstrip('>').lstrip()
			while (lineIndex + 1 < len(self.lines)) and (self.identify(self.lines[lineIndex + 1]) == ElementType.blockquote):
				newLine = self.lines[lineIndex + 1].lstrip('>').lstrip()
				if newLine == '':
					if tempString.startswith('#'):
						tag = 'h' + str(tempString[:6].count('#'))
					else:
						tag = 'p'

					string += ('\n<' + tag + '>' + tempString.lstrip('#') + '</' + tag + '>')
					tempString = ''
				else:
					tempString += newLine

				lineIndex += 1

			string += ('\n<p>' + tempString + '</p>')

			newElement.setText(string)

		self.elements.append(newElement)

		return lineIndex + 1



	def parseLines(self):
		currentlyIn = None

		i = 0

		while i < len(self.lines):
			lineType = self.identify(self.lines[i])

			i = self.handle(lineType, i)

			# if currentlyIn

			# self.feed(line)
			# self.elements.append(MarkupElement(line, i))

	def parseFile(self, fileObj):
		if isinstance(fileObj, file):
			fileObj = fileObj.read()

		self.lines = fileObj.split('\n')

		self.parseLines()

	def writeToFile(self, fileObj):
		for element in self.elements:
			fileObj.write(str(element))
			fileObj.write('\n')
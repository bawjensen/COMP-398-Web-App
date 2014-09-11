from helpers import consistsEntirelyOf, isUnderlineForHeader
from MarkupElements import ListElement, HeaderElement, ParagraphElement, BlockQuoteElement, PreformattedCodeElement

import re

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

class MarkdownParser(object):
	def __init__(self):
		self.elements = []

		self.listLineStart = re.compile(r'[\+\-\*]')
		self.blockQuoteLineStart = re.compile(r'[\>]')
		self.headerLineStart = re.compile(r'#')
		self.preCodeLineStart = re.compile(r'\s{4}|\t')

	def handleList(self, linesList, currIndex):
		listItems = []

		match = self.listLineStart.match(self.lines[currIndex])

		while (currIndex < len(linesList)) and (match):
			line = linesList[currIndex]

			listToken = match.string[match.start():match.end()]
			listItems.append(line.lstrip(listToken).lstrip(' '))

			if currIndex + 1 < len(linesList):
				match = self.listLineStart.match(linesList[currIndex + 1])
			else:
				match = None

			currIndex += 1

		self.elements.append(ListElement(listItems, ordered=False))

		return currIndex

	def handleHeader(self, linesList, currIndex):
		line = linesList[currIndex]

		headerLevel = 0
		for letter in line:
			if letter == '#':
				headerLevel += 1
			else:
				break

		if headerLevel > 6:
			print 'Um... You can\'t make a header smaller than six levels:', line
			exit(1)

		if headerLevel == 0:
			nextLine = linesList[currIndex + 1]

			underlineCharacter = nextLine.lstrip()[0]

			headerLevel = 1 if (underlineCharacter == '=') else 2

			currIndex += 1 # Need to increment another index if we have an underlined header

		self.elements.append(HeaderElement(line.lstrip('#').lstrip(), headerLevel))

		currIndex += 1

		return currIndex

	def handleParagraph(self, linesList, currIndex):
		paragraphContents = ''
		while (currIndex < len(linesList)) and (linesList[currIndex].strip() != ''):
			line = linesList[currIndex].strip()

			paragraphContents += (line + ' ')

			currIndex += 1

		self.elements.append(ParagraphElement(paragraphContents.rstrip(' ')))

		return currIndex

	def handleBlockQuote(self, linesList, currIndex):
		newLinesList = []

		match = self.blockQuoteLineStart.match(linesList[currIndex])

		while (currIndex < len(linesList)) and (match):
			line = linesList[currIndex].lstrip('>').lstrip()

			newLinesList.append(line)

			if currIndex + 1 < len(linesList) and (match):
				match = self.blockQuoteLineStart.match(linesList[currIndex + 1])
			else:
				match = None

			currIndex += 1

		# tempIndex = 0
		# while tempIndex < len(newLinesList):
		oldLength = len(self.elements)

		self.parseLines(newLinesList)

		newElements = self.elements[oldLength:]
		self.elements = self.elements[:oldLength]

		self.elements.append(BlockQuoteElement(newElements))

		return currIndex

	def handlePreformattedCode(self, linesList, currIndex):
		contents = ''

		match = self.preCodeLineStart.match(linesList[currIndex])

		while (currIndex < len(linesList)) and bool(match):
			line = linesList[currIndex]

			contents += (line.strip() + ' ')

			if currIndex + 1 < len(linesList):
				match = self.preCodeLineStart.match(linesList[currIndex + 1])
			else:
				match = None

			currIndex += 1

		self.elements.append(PreformattedCodeElement(contents.rstrip(' ')))

		return currIndex

	def parseLines(self, linesList):
		i = 0
		while i < len(linesList):
			line = linesList[i]

			if line.strip() == '':
				i += 1
				continue

			if i + 1 < len(linesList):
				nextLine = linesList[i + 1]

			if self.listLineStart.match(line):
				print line, 'was a list'
				i = self.handleList(linesList, i)

			elif self.headerLineStart.match(line) or (i + 1 < len(linesList) and isUnderlineForHeader(nextLine)):
				print line, 'was a header'
				i = self.handleHeader(linesList, i)

			elif self.blockQuoteLineStart.match(line):
				print line, 'was a block quote'
				i = self.handleBlockQuote(linesList, i)

			elif self.preCodeLineStart.match(line):
				print line, 'was a preformatted code block'
				i = self.handlePreformattedCode(linesList, i)

			else:
				print line, 'was a paragraph'
				i = self.handleParagraph(linesList, i)

		return i



	def parseFile(self, fileObj):
		if isinstance(fileObj, file):
			fileObj = fileObj.read()
		elif isinstance(fileObj, str):
			fileObj = open(fileObj, 'r').read()

		self.lines = fileObj.split('\n')

		self.parseLines(self.lines)


	def writeToFile(self, fileObj):
		tempOpened = False
		if isinstance(fileObj, str):
			fileObj = open(fileObj, 'w')
			tempOpened = True

		for element in self.elements:
			fileObj.write(str(element))
			fileObj.write('\n')

		if tempOpened:
			fileObj.close()


def main():
	parser = MarkdownParser()
	parser.parseFile('tiny.md')

	parser.writeToFile('tiny.html')

if __name__ == '__main__':
	main()
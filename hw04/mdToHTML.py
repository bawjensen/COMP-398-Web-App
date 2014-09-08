import os
import string
import sys
from mdParser import MarkdownParser

def nextLineComposedOf(possibleUnderlineString, char):
	return ((possibleUnderlineString != '') and (possibleUnderlineString.count(char) == len(possibleUnderlineString)))

def main():
	if len(sys.argv) < 2:
		print "File name of the input markdown file was not provided. Please use in the format:"
		print "python mdToHTML.py <filename>"
		exit(1)
	elif len(sys.argv) > 2:
		print "Too many parameters provided. Please use in the format:"
		print "python mdToHTML.py <filename>"
		exit(1)


	inFilePath = sys.argv[1]
	outFilePath = os.path.join(os.path.split(inFilePath)[0], 'sample.html')

	parser = MarkdownParser()

	with open(inFilePath, 'r') as inFile:
		parser.parseFile(inFile)

	with open(outFilePath, 'w') as outFile:
		parser.writeToFile(outFile)


if __name__ == '__main__':
	main()
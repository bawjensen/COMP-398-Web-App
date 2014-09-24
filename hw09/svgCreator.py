import operator

def createSVGCircle(positionX, positionY, size):
	svgCircle = '<circle'

	svgCircle += ' cx="' + str(positionX) + '"'
	svgCircle += ' cy="' + str(positionY) + '"'
	svgCircle += ' r="' + str(size) + '"'

	svgCircle += ' fill="#00FF00"'

	svgCircle += '/>'

	return svgCircle


def createSVGCircleLabel(positionX, positionY, label, count, size):
	font_size = 30

	svgLabel = '<text'

	svgLabel += ' x="' + str(positionX) + '"'
	svgLabel += ' y="' + str(positionY - size - font_size*.2) + '"'
	svgLabel += ' font-size="' + str(font_size) + '"'
	svgLabel += ' text-anchor="middle"'
	svgLabel += ' fill="black"'

	svgLabel += '>'

	svgLabel += label + ':' + str(count)

	svgLabel += '</text>'

	return svgLabel


def main():
	with open('enrollment.json', 'r') as inFile:
		fileContents = inFile.read().lstrip('{').rstrip('}').split(',')

		enrollmentDict = dict(
			(
				(k.strip().strip('"'), int(v.strip().strip('"'))) for k, v in 
					(item.split(': ') for item in fileContents
				)
			)
		)

	# departments = [key for key, value in sorted(enrollmentDict.iteritems(), key=operator.itemgetter(1), reverse=True)]
	departments = enrollmentDict.keys()

	svgElement = """<svg version="1.1"
	baseProfile="full"
	width="1300" height="1300"
	xmlns="http://www.w3.org/2000/svg">
	"""

	scalar = 0.15
	spacing = 200

	for i in xrange(6):
		for j in xrange(6):
			yPos = (j+1) * spacing
			xPos = (i+1) * spacing
			departmentLabel = departments[i + j*6]
			count = enrollmentDict[departmentLabel]
			size = count * scalar

			svgElement += '\n\t' + createSVGCircle(xPos, yPos, size)
			svgElement += '\n\t' + createSVGCircleLabel(xPos, yPos, departmentLabel, count, size)

	svgElement += '\n</svg>'

	with open('unsorted.svg', 'w') as outFile:
		outFile.write(svgElement)

if __name__ == '__main__':
	main()
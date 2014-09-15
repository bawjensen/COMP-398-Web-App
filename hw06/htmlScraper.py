import re

from bs4 import BeautifulSoup

with open('testing.html', 'r') as inFile:
	soup = BeautifulSoup(inFile.read(), 'html.parser') # Have to use html.parser, because it handles the broken HTML better

classLabelTest = re.compile(r'[A-Z][A-Z][A-Z][A-Z]?-[0-9][0-9][0-9]')
departmentMatcher = re.compile(r'[A-Z][A-Z][A-Z][A-Z]?')

departmentEnrollment = {}

allRows = soup.find_all('tr')

for i in xrange(len(allRows)):
	row = allRows[i]

	possibleClassLabel = row.find('td').getText().encode('utf-8').strip()

	if classLabelTest.match(possibleClassLabel):
		match = departmentMatcher.match(possibleClassLabel)
		department = possibleClassLabel[match.start():match.end()]

		if i + 2 < len(allRows):
			enrollmentElements = allRows[i+2].find_all('td')

			if len(enrollmentElements) < 3:
				enrollmentElements = allRows[i+1].find_all('td')

		numEnrolled = int(enrollmentElements[2].getText().replace('Seats Taken: ', ''))

		if department not in departmentEnrollment:
			departmentEnrollment[department] = numEnrolled
			pass
		else:
			departmentEnrollment[department] += numEnrolled
			pass

with open('enrollment.json', 'w') as outFile:
	outFile.write(str(departmentEnrollment).replace('\'', '"'))


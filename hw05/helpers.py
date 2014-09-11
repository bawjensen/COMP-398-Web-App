def consistsEntirelyOf(line, char):
	return (line != '') and (line.count(char) == len(line))

def isUnderlineForHeader(line):
	line = line.strip()
	return (line != '') and (line[0] == '-' or line[0] == '=') and (line.count(line[0]) == len(line))
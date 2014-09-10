import re

listLineStarter = re.compile(r'[\*\-\+]')

print listLineStarter.match('hahahaha')

if (None):
	print 'yay'
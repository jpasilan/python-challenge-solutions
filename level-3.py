#! /usr/bin/env python

import re

code = ""
f = open('level-3.txt', 'r')
for line in f:
	code += line.strip()

print "".join(re.findall("(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])", code))

# Close file
f.close()

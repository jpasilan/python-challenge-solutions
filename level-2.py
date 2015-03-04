#! /usr/bin/env python

import re

code = ""
f = open('level-2.txt', 'r')
for line in f:
	code += line.strip() # Strip new lines

# Find all lowercase characters in the code
print "".join(re.findall('[a-z]', code))

# Closing the file
f.close()
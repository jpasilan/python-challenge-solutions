#! /usr/bin/env python

import urllib2, re

ending = 0

while True:
	page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(ending))
	page_text = page.read()

	number = "".join(re.findall("\d+", page_text))
	if number == "":
		print page_text
		break
	else:
		ending = number
		print page_text

#! /usr/bin/env python

import urllib2, pickle

url = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p");
p = pickle.load(url)
for line in p:
	print "".join(char * number for char, number in line)

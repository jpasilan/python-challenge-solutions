#! /usr/bin/env python

import os, zipfile, re
from urllib2 import urlopen, URLError, HTTPError

def download_file(url):
	try:
		f = urlopen(url)
		print "Downloading", url

		with open(os.path.basename(url), 'wb') as local_file:
			local_file.write(f.read())

	except HTTPError, e:
		print "HTTP Error:", e.code
	except URLError, e:
		print "URL Error:", e.reason

def main():
	download_file("http://www.pythonchallenge.com/pc/def/channel.zip")
	
	zip = zipfile.ZipFile('channel.zip', 'r')
	nothing = "90052"
	comments = []

	while True:
		try:
			file_name = "%s.txt" % nothing
			text_in_file = zip.read(file_name)
			nothing = "".join(re.findall("\d+", text_in_file))
			comments.append(zip.getinfo(file_name).comment)
			print nothing
		except KeyError:
			# Stop when file in zip is not found.
			break

	print "".join(comments)



if __name__ == "__main__":
	main()
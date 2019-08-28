#!/usr/bin/python
import sys
# print sys.argv

try:
	try:
		print sys.argv[2]
	except Exception as a:
		print "No second argument is passed"
except Exception as b:
	try:
		print sys.argv[1]
	except Exception as e:
		print "No argument is passed"

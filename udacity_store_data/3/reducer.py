#!/usr/bin/python

import sys

def reducer():
	
	oldKey = None
	maxSale = None
	
	for line in sys.stdin:
		data= line.strip().split("\t")
		if(len(data)!=2):
			continue

		thisKey= data[0]
		thisSale = float(data[1])
		if(not oldKey):
			oldKey = thisKey
			maxSale = thisSale

		if (oldKey != thisKey):
			print ("{}\t{}".format(oldKey,maxSale))
			oldKey= thisKey
			maxSale = thisSale
		if(thisSale > maxSale):
			maxSale = thisSale

	if(oldKey!=None):	
		print("{}\t{}".format(oldKey,maxSale))

reducer()

#!/usr/bin/python

import sys

def reducer():
	
	oldKey = None
	totalSales = 0
	
	for line in sys.stdin:
		data= line.strip().split("\t")
		if(len(data)!=2):
			continue
	
		thisKey,thisSale = data
		thisSale=float(thisSale)

		if (oldKey and oldKey != thisKey):
			print ("{}\t{}".format(oldKey,totalSales))
			oldKey=thisKey
			totalSales = 0


		oldKey = thisKey
		totalSales += float(thisSale)

	if(oldKey!=None):	
		print("{}\t{}".format(oldKey,totalSales))

reducer()

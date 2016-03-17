#!/usr/bin/python

import sys

def reducer():
	
	totalSale = 0
	counter = 0
	
	for line in sys.stdin:
		data= line.strip().split("\t")
		if(len(data)!=1):
			continue

		totalSale = totalSale + float(data[0])
		counter = counter + 1;
	
	print "Total Sales", totalSale
	print "Total number of Sales", counter

reducer()

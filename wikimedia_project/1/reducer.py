#!/usr/bin/python
import sys

oldLanguage=None
oldPage=None
oldViews=None

for line in sys.stdin:
	data = line.strip().split("\t")
	language,page,views = data
	
	if(len(data)!=3):
		continue

	if (not oldLanguage):
		oldLanguage=language
		oldViews=views
		oldPage=page
	
	if(oldLanguage!=language):
		print("{}\t{}\t{}".format(oldLanguage,oldPage,oldViews))
		oldLanguage=language
		oldViews=views
		oldPage=page
	if(views > oldViews):	
		oldViews=views
		oldPage=page

if(oldLanguage != None):
	print("{}\t{}\t{}".format(oldLanguage,oldPage,oldViews))
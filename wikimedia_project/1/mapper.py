#!/usr/bin/env python

import sys

# Read each line from STDIN
for line in sys.stdin:
   data = line.strip().split()
   if len(data) != 4 :
	continue

   language,page,views,size = data
   print '{}\t{}\t{}'.format(language,page,views)
  


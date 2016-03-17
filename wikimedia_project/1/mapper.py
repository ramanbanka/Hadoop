
#!/usr/bin/python
'''
The shebang line above is necessary in this script. It is because it tells the jar file about this scrpit.
'''

#imprort the system library
import sys


# Read each line from STDIN
def mapper():
	for line in sys.stdin:

   		data = line.strip().split()
   		if len(data) != 4 :
			continue

		language,page,views,size = data
  		print '{}\t{}\t{}'.format(language,page,views)
  
mapper()

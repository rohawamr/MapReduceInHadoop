#!/usr/bin/env python

import sys
import string

num_count = 0
old_num = None

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	if old_num != key:
		if old_num:
			print '%s\t%s' % ( old_num,num_count)
		num_count = 0
	old_num = key
	try:
		num_count = num_count + int(val)
	except:
		continue
print '%s\t%s' % (old_num,num_count)

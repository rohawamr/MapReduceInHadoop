#!/usr/bin/env python

import sys
import string

word_count = 0
old_word = None
c=0

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	if old_word != key:
		if old_word:
			if old_word == 'AvgSenLen':
				word_count=word_count/c
				print '%s\t%s' % (old_word,word_count)
			else:
				print '%s\t%s' % (old_word,word_count)
		word_count = 0
	old_word = key
	try:	
		if key == 'AvgSenLen':
			word_count = word_count + int(val)
			c+=1
		else:
			word_count = word_count + int(val)
	except:
		continue



if old_word == 'AvgSenLen':
	word_count=word_count/c
	print '%s\t%s' % (old_word,word_count)
else:
	print '%s\t%s' % (old_word,word_count)

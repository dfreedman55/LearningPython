#!/usr/bin/env python

import sys

ipadd = sys.argv[1].split('.')
print ipadd

for i,v in enumerate(ipadd):
	ipadd[i] = bin(int(ipadd[i]))

print ipadd

#grab item from list 
for i,v in enumerate(ipadd):
	ipadd[i] = ipadd[i].lstrip('0b')
	count = 8 - len(ipadd[i])
	addzeros = '0' * count
	ipadd[i] = addzeros + ipadd[i]

print '.'.join(ipadd)

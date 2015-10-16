#!/usr/bin/env python

import sys

ipadd = sys.argv[1].split('.')
print ipadd

for i, v in enumerate(ipadd):
	ipadd[i] = bin(int(ipadd[i]))

print '.'.join(ipadd)

#!/usr/bin/env python

import sys

ipadd = sys.argv[1].split('.')
print ipadd

for i,v in enumerate(ipadd):
	ipadd[i] = bin(int(ipadd[i]))

print '.'.join(ipadd)

## HONESTLY I'M NOT SURE HOW I WOULD USE FLOW CONTROL TO MAKE THIS PROGRAM SIMPLER

#!/usr/bin/env python

print '%-15s %-15s' % ('ip_prefix', 'as_path')

with open('input-exercise3.txt', 'r') as f:
	lines = f.readlines()
	for item in lines:
		templist = item.split('157.130.10.233')
		templist[0] = templist[0].strip().split(' ')[-1]
		templist[1] = templist[1].strip().split(' ')[1:-1]
		print '%-15s %-15s' % (templist[0], templist[1])

#!/usr/bin/env python

import re

mydict = {}

with open('ospf_data.txt', 'r') as f:
    output = f.read()

interface = re.findall(r'(.+?) is (.+?), line protocol is (.+)', output)
ip_address = re.findall(r'Internet Address (.+?),', output)
area = re.findall(r', Area (.+?),', output)
type = re.findall(r'Network Type (.+?),', output)
cost = re.findall(r' Cost: (.+?)', output)
hello = re.findall(r'Timer intervals configured, Hello (.+?), Dead', output)
dead = re.findall(r', Dead (.+?), Wait', output)

j = 0
if len(hello) < len(ip_address):
        diff = int(len(ip_address)) - int(len(hello))
        while j < diff:
                hello.insert(0, 'loopback')
		dead.insert(0, 'loopback')
		j += 1

print interface
print ip_address
print area
print type
print cost
print hello
print dead

def print_items():
    i = 0
    while i < len(ip_address):
	print '%-5s %-15s' % ('Int:', interface[i][0])
	print '%-5s %-15s' % ('IP:', ip_address[i])
	print '%-5s %-15s' % ('Area', area[i])
	print '%-5s %-15s' % ('Type', type[i])
	print '%-5s %-15s' % ('Cost', cost[i])
	if 'Loopback' in interface[i][0]:
		pass
	else:
		print '%-5s %-15s' % ('Hello', hello[i])
		print '%-5s %-15s' % ('Dead', dead[i])
	print ''
	i += 1

print_items()

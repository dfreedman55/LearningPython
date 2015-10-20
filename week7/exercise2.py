#!/usr/bin/env python

import re

mydict = {}

with open('ospf_single_interface.txt', 'r') as f:
    output = f.read()

interface = re.search(r'(.+?) is ', output)
interface = interface.group(1)
mydict['interface'] = interface

ip_address = re.search(r'Internet Address (.+?),', output)
ip_address = ip_address.group(1)
mydict['ip_address'] = ip_address

area = re.search(r', Area (.+?),', output)
area = area.group(1)
mydict['area'] = area

type = re.search(r'Network Type (.+?),', output)
type = type.group(1)
mydict['type'] = type

cost = re.search(r' Cost: (.+?)', output)
cost =cost.group(1)
mydict['cost'] = cost

timers = re.search(r'Timer intervals configured, Hello (.+?), Dead (.+?), Wait (.+?), Retransmit (.+)', output)
hello =  timers.group(1)
dead = timers.group(2)
mydict['hello'] = hello
mydict['dead'] = dead

for k,v in mydict.items():
    print k,v

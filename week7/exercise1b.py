#!/usr/bin/env python

import re

with open('sw1_cdp.txt', 'r') as f:
    output = f.read()

mydict = {}

hostname = re.findall(r'Device ID: (.+)', output)
mydict['remote_hosts'] = hostname

remote_ip_address = re.findall(r'IP address: (.+)', output)
mydict['IPs'] = remote_ip_address

model = re.findall(r'Platform: (.+?),', output)
mydict['platform'] = model

for k,v in mydict.items():
    print k,v


#!/usr/bin/env python

import re

with open('r1_cdp.txt', 'r') as f:
    output = f.read()

mydict = {}

hostname = re.search(r'Device ID: (.+)', output)
hostname = hostname.group(1)
mydict['hostname'] = hostname

remote_ip_address = re.search(r'IP address: (.+)', output)
remote_ip_address = remote_ip_address.group(1)
mydict['remote_ip'] = remote_ip_address

model = re.search(r'Platform: (.+?),', output)
model = model.group(1).split(' ')[-1]
mydict['model'] = model

vendor = re.search(r'Platform: (.+?),', output)
vendor = vendor.group(1).split(' ')[0]
mydict['vendor'] = vendor

device_type = re.search(r'Capabilities: (.+)', output)
device_type = device_type.group(1)

if 'Router' in device_type:
    device_type = 'Router'
else:
    device_type = 'Switch'

mydict['device_type'] = device_type

for k,v in mydict.items():
    print k,v


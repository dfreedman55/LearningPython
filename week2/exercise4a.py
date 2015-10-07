#!/usr/bin/env python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios = cisco_ios.split(',')
print cisco_ios[2].strip().split(' ')[1]

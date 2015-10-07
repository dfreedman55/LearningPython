#!/usr/bin/env python

import re

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios = re.search(r'Cisco IOS Software, (.+?), (.+?), (.+)', cisco_ios)
print cisco_ios.group(2).split(' ')[-1]

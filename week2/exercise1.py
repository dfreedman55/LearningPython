#!/usr/bin/env python

input_ip = str(raw_input("Please enter an IP address:"))
input_ip = input_ip.split('.')
if len(input_ip) == 3:
	input_ip.append('0')
if len(input_ip) == 4:
	input_ip[3] = '0'
first_octet = int(input_ip[0])
first_binary = bin(first_octet)
first_hex = hex(first_octet)
print '.'.join(input_ip)
print '%-20s %-20s %-20s' % ('NETWORK', 'FIRST_BINARY', 'FIRST_HEX')
print '%-20s %-20s %-20s' % ('.'.join(input_ip), first_binary, first_hex)

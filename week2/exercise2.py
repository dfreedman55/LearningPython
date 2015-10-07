#!/usr/bin/env python

input = raw_input("Please enter an IP adddress:")
input = input.split('.')
for i,v in enumerate(input):
  input[i] = bin(int(v))
print '%s %25s %25s %25s' % ('first_octet', 'second_octet', 'third_octet', 'fourth_octet')
print '%s %25s %25s %25s' % (input[0], input[1], input[2], input[3])

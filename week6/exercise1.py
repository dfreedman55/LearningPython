#!/usr/bin/env python

def product(x,y,z=1):
	result = x * y * z
	print 'X = %s, Y = %s, Z = %s' % (x, y, z)
	print 'Result of x * y * z: %s' % result

if __name__ == '__main__':
	product(2,3,4)
	product(z=4,y=2,x=3)
	product(2,y=3,z=4)
	product(2,3)

#!/usr/bin/env python

def newfunc(ipadd):
	four = fouroctets(ipadd)

	if four == True:
		invalid = False
		first = int(ipadd.split('.')[0])
		second = int(ipadd.split('.')[1])
		third = int(ipadd.split('.')[2])
		fourth = int(ipadd.split('.')[3])
		if bool(first) and bool(second) and bool(third) and bool(fourth):
			if first not in range(1,224):
				invalid = True
			if first == 127:
				invalid = True
			if first == 169 and second == 254:
				invalid = True
			if (second not in range(0,256)) or (third not in range(0,256)) or (fourth not in range(0,256)):
				invalid = True
		else:
			pass

	else:
		invalid = True

	if invalid != True:
		print 'TRUE:  %s  is a valid IP address' % ipadd
	if invalid == True:
		print 'FALSE:  %s  is an invalid IP address' % ipadd

def fouroctets(ipadd):
		if ipadd.count('.') != 3:
			return False
		elif ipadd.split('.')[3] == '':
			return False
		else:
			return True

if __name__ == '__main__':
	ipadd = '10.20.30'
	newfunc(ipadd)
	ipadd = '10.20.30.'
	newfunc(ipadd)
	ipadd = '224.20.30.40'
	newfunc(ipadd)
	ipadd = '127.20.30.40'
	newfunc(ipadd)
	ipadd = '169.254.30.40'
	newfunc(ipadd)
	ipadd = '10.256.30.40'
	newfunc(ipadd)
	ipadd = '10.20.256.40'
	newfunc(ipadd)
	ipadd = '10.20.30.256'
	newfunc(ipadd)
	ipadd = '10.20.30.40'
	newfunc(ipadd)

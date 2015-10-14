#!/usr/bin/env python

def main():
	prompt = True
	while prompt == True:
		ipadd = raw_input("Please enter an ip address: ")
	
		try:
			if ipadd.count('.') != 3:
				invalid = True
			elif ipadd.split('.')[3] == '':
				invalid = True
			else:
				invalid = False
				first = int(ipadd.split('.')[0])
				second = int(ipadd.split('.')[1])
				third = int(ipadd.split('.')[2])
				fourth = int(ipadd.split('.')[3])
		except ValueError:
			print 'ValueError:  The IP address must contain 4 octets.'
		except IndexError:
			print 'IndexError:  The IP address must contain 4 octets.'
	
		if invalid == True:
			print 'The IP address must contain 4 octets.'
		else:
			if first not in range(1,224):
				print 'The first octet must be between 1-223.'
				invalid = True
			if first == 127:
				print 'The first octet cannot be 127.'
				invalid = True
			if first == 169 and second == 254:
				print 'The IP address cannot be in the 169.254.X.X address space.'
				invalid = True
			if (second not in range(0,256)) or (third not in range(0,256)) or (fourth not in range(0,256)):
				print 'The last three octets must range between 0-255.'
				invalid = True
		if invalid != True:
			print ipadd + ' is a valid IP address'
			prompt = False


if __name__ == '__main__':
	main()



#!/usr/bin/env python

def listconv(list):
	for i,v in enumerate(list):
		mydict[i] = v
	print mydict

if __name__ == '__main__':
	mylist = ['dan', 'david', 'kristen', 'paul']
	mydict = {}
	listconv(mylist)

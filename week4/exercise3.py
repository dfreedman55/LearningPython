#!/usr/bin/env python


def main():
	parsestring(uptime1)
	sumsec(stats)
	parsestring(uptime2)
	sumsec(stats)
	parsestring(uptime3)
	sumsec(stats)
	parsestring(uptime4)
	sumsec(stats)


def yrs2sec(numyrs):
	seconds = numyrs * 12 * 4 * 7 * 24 * 60 * 60
	stats['years'] = seconds


def mth2sec(nummth):
	seconds = nummth * 4 * 7 * 24 * 60 * 60
	stats['months'] = seconds


def wks2sec(numwks):
	seconds = numwks * 7 * 24 * 60 * 60
	stats['weeks'] = seconds


def dys2sec(numdys):
	seconds = numdys * 24 * 60 * 60
	stats['days'] = seconds


def hrs2sec(numhrs):
	seconds = numhrs * 60 * 60
	stats['hours'] = seconds


def min2sec(nummin):
	seconds = nummin * 60
	stats['minutes'] = seconds


def sumsec(stats):
	total = int(0)
	for k, v in stats.items():
		if type(v) != type('string'):
			total = total + v
	print stats
	print '\n'
	print 'Total Seconds for %s is: %s' % (stats['devicename'], total)
	print '\n'


def parsestring(uptimestr):
	stats['devicename'] = uptimestr.split(' ')[0]
	if 'year' in uptimestr:
		numyrs = int(uptimestr.split('year')[0].strip().split(' ')[-1])
		yrs2sec(numyrs)
	if 'month' in uptimestr:
		nummth = int(uptimestr.split('month')[0].strip().split(' ')[-1])
		mth2sec(nummth)
	if 'week' in uptimestr:
		numwks = int(uptimestr.split('week')[0].strip().split(' ')[-1])
		wks2sec(numwks)
	if 'day' in uptimestr:
		numdys = int(uptimestr.split('day')[0].strip().split(' ')[-1])
		dys2sec(numdys)
	if 'hour' in uptimestr:
		numhrs = int(uptimestr.split('hour')[0].strip().split(' ')[-1])
		hrs2sec(numhrs)
	if 'minute' in uptimestr:
		nummin = int(uptimestr.split('minute')[0].strip().split(' ')[-1])
		min2sec(nummin)

if __name__ == '__main__':
	uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
	uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
	uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
	uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'
	stats = {'devicename': '', 'years': '', 'months': '', 'weeks': '', 'days': '', 'hours': '', 'minutes': ''}
	main()

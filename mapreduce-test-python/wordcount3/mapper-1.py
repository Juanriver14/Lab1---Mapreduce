#!/usr/bin/python
# --*-- coding:utf-8 --*--

from operator import itemgetter
import sys
hours = []

for line in sys.stdin:
    hour_ip,num = line.split("\t")
    hours = hour_ip[:7]; ip = hour_ip[7:]
    print('{}\t{}'.format(hours, ip + '. ' + num))

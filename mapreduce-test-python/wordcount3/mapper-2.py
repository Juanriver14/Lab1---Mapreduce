#!/usr/bin/env python
#!/usr/bin/python3

from operator import itemgetter
import sys

for line in sys.stdin:
  hour_ip,num = line.split("\t")
  hours = hour_ip[:7]; ip = hour_ip[7:]
  print('{}\t{}'.format(hour_ip, ip + ', ' + num))

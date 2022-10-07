#!/usr/bin/env python
import sys
from operator import itemgetter

reduce_2_output = {}
for line in sys.stdin:
  line = line.strip()
  try:
   hour, ip_num = line.split("\t")
   reduce_2_output[hour] = reduce_2_output.get(hour, "") + ip_num + '\n'
   pass

for hour, info in reduce_2_output.items():
    ip_num_dict = {}
    info = info.strip().split('\')
  for line in info:
      ip, num = line.split(',')
      num = int(num)
      ip_num_dict[ip] = num
  ip_num_dict = sorted(ip_num_dict.items(), key= lambda x: x[1], reverse=True)
  reduce_2_output[hour] = ip_num_dict[:3]
ordered_numbers = list(sorted(reduce_2_output.keys()))
                              
                              
                              
for hour in ordered_numbers:
  info = reduce_2_output[hour]
  for i in info:
     print("{}\t{}\t{}". format(hour, i[0], i[1]))


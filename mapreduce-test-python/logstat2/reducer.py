#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
hour_flag = ''
dict_hour = {}

for hour_ip, count in sorted_dict_ip_count:
    hour, ip = hour_ip.split(" ")
    if not dict_hour.get(hour):
        dict_hour[hour] = {hour_ip: count}
    else:
        dict_hour[hour].update({hour_ip: count})

for hour in dict_hour:
      ips_in_current_hour = sorted(dict_hour[hour].items(),  key=itemgetter(1), reverse=True)
      print("Top 3 IP at {hour}:")
      for i in range(0,3):
        print(ips_in_current_hour[i])
      print("\n\n")

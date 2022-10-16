#!/usr/bin/python
# Reducer
from operator import itemgetter
import sys

# it will store the reducer output
dict_ip_count = {} 
for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t') #splits the formatted string line into variables as ip and num
    try:
      num = int(num) #convert num into an integer 
      dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num # iterates throght a dictionary saying that if it is empty for the ip key it wil retieve 0 sums it with the values inside num if it is not empty it will sum the stored value wit hthe value stored in sum 
      # {"[10:00] 100.3.4.5": 1}
        
    except ValueError:
        pass
  
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0)) # will sorts the dictionary by hour 

hour_flag = ''

dict_hour = {}

for hour_ip, count in sorted_dict_ip_count:
  # Getting the hour and the  ip separate
  hour = hour_ip[:7]
  ip = hour_ip[7:]
  
  if not dict_hour.get(hour):
    dict_hour[hour] = {hour_ip: count}
  else:
    dict_hour[hour].update({hour_ip: count})

# Making sure the output is sorted by hour
for hour in sorted(dict_hour.keys()):
  ips_in_current_hour = sorted(dict_hour[hour].items(),  key=itemgetter(1), reverse=True)
  print 'Top 3 IP at %s' % (hour)
  for i in range(0,3):
    x = ' -> '.join(str(v) for v in ips_in_current_hour[i])
    print x
  print "\n\n"

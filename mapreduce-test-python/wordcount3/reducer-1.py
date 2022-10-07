#!/usr/bin/env python
#!/usr/bin/python3
from operator import itemgetter
import sys

reducer_1_output = {}
for line in sys.stdin:
  line = line.strip()
  hour_ip, num = line.split("\t")
  num = int(num)

  reducer_1_output[hour_ip] = reducer_1_output.get(hour_ip,0) + num
sorted_reducer_1_output = sorted(reducer_1_output.items(), key=itemgetter(0))

for hour_ip, num in sorted_reducer_1_output:
  print("{}\t{}\".format9=(hour_ip, num))

#!/usr/bin/env python

import sys
import string

count = 1.0
avg = 0.0
summ = 0.0
hour = None
date = None

output = {}
for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if hour != key:
     if hour:
         avg = summ / count
         print '%s\t%s\t%s\t%s' % (hour,avg,summ,count)
         output[avg]= hour
         avg = 0.0
         summ = 0.0
         count = 1.0
  hour = key
  try:
     summ = summ + 1
     if date != val:
       if date:
          count = count + 1
     date = val
  except:
     continue
avg = summ / count
print '%s\t%s\t%s\t%s' % (hour,avg,summ,count)
output[avg] = hour
print 'PrezOno tweeted in the hour %s with the maximum average of %s' % (output[max(output)],(max(output))) 
  
 




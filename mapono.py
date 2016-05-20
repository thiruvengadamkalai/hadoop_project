#!/usr/bin/env python

import sys
import string
import json

for line in sys.stdin:
    tweet = json.loads(line)    
    dt = tweet['created_at']
    tweeter = tweet['user']['screen_name'].strip().lower()
    hour = dt[11:13]
    date = dt[4:10]
    if tweeter == "prezono":
      print '%s\t%s' % ( hour, date)

   


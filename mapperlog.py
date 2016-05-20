#!/usr/bin/env python
import sys
import string
import json
#f = open('part-00140','r+')
for line in sys.stdin:
  tweets = json.loads(line)
  tweeter = tweets ['user']['screen_name'].strip().lower()

  message=tweets['text']
  #print message.encode('utf_8')
  stringl = len(message)
  #print stringl
  if tweeter == "prezono":
  
    print '%s\t%s' % ('ono',stringl)
  else:
    print '%s\t%s' % ('notono',stringl)
    
    
    
    
 

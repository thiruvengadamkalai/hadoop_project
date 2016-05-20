#!/usr/bin/env python
from __future__ import division
import sys
import string
onores = 0
onoct = 0
notonores = 0
notonoct = 0
for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  if key == "ono":
    onores = onores + int(val)
    onoct = onoct + 1
  else:
    notonores = notonores + int(val)
    notonoct = notonoct + 1
  #presult1 = sum(presult)
  #presult2 = len(val)
  
onoress= onores/onoct
notonoress = notonores / notonoct
proportion = onoress / notonoress  
print onoress,onores,onoct
print notonoress,notonores,notonoct
print proportion
#print result

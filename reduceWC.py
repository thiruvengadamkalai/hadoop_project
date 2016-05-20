#!/usr/bin/env python
from __future__ import division
import sys
import string

for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  result=int(val)/int(key)
  print result

#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

information = []

for line in open(sys.argv[1]):
    
    fields = line.split()
    name = fields[0]
    ratio = fields[2]
    gaps = int(fields[5])
    information.append((name, ratio, gaps))
  
    
print information




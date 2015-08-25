#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015-homework/day2/day2-lunch/SRR072893.sam"

f = open (filename)

for line in f:
    if "SRR" in line:
        print sum(1 for line in f)







    
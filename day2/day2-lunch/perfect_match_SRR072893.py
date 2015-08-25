#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015-homework/day2/day2-lunch/SRR072893.sam"

f = open (filename)

num=0

for lines in f:
    if "NM:i:0" in lines:
        num += 1
print num
        



#print sum(1 for lines in f)
    
#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015-homework/day2/day2-lunch/SRR072893.sam"

f = open (filename)



chromosome_counts = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}


for lines in f:
    columns = lines.split()
    chromosome = columns[2]
    if "@" in lines:
        #to avoid the header
        pass
    elif chromosome in chromosome_counts:
           chromosome_counts[chromosome] += 1
    else:
        pass


print chromosome_counts


#I'm getting an error that says "list index out of range" but I can't figure out




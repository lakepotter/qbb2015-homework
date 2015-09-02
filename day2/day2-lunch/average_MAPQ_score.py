#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015/genomes/SRR072893_2.sam"

f = open (filename)

#average MAPQ score - get all the MAPQ scores divided by the total number of counts


count = 0
total_MAPQ = 0

for lines in f:
    
    if "@" in lines:
        #to avoid the header
        pass
    
    else:
        count += 1
        column = lines.split()
        MAPQ = column[4]
        MAPQ = int(MAPQ)
        total_MAPQ += MAPQ

average = total_MAPQ/count
print average
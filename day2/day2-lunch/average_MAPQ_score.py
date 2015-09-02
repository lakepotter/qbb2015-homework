#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015-homework/day2/day2-lunch/SRR072893.sam"

f = open (filename)

#average MAPQ score - get all the MAPQ scores divided by the total number of counts

MAPQ = 0
count = 0

for lines in f:
    columns = lines.split()
    #print columns[0:5] - this seems to be working...
    MAPQ_value = columns[4]
    if "@" == columns[0]:
        #to avoid the header
        pass
    else:
        MAPQ += int(MAPQ_value)
        count += 1


print MAPQ/count
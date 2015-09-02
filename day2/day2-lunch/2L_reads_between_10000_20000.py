#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015/genomes/SRR072893_2.sam"

f = open (filename)

count = 0

for line in f:
    if "@" in line:
        pass
    else:
        columns = line.split()
        if columns[2] == "2L":
            if int(columns[3])<20000 and int(columns[3])>10000:
                count +=1 
        else:
            pass

print count


#okay, just make your column[2] == "2L" and 10000< int(column[3])<20000 (I might have to write this a different way) and then print
    
#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015/genomes/SRR072893_2.sam"

f = open (filename)



chromosome_counts = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}


for lines in f:
    if "@" in lines:
        #to avoid the header
        pass
   
    else:
        columns = lines.split()
        #print lines
        chromosome = columns[2]
        
        if chromosome in chromosome_counts:
           chromosome_counts[chromosome] += 1
        else:
            pass


print chromosome_counts






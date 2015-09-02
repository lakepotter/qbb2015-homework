#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015/genomes/SRR072893.sam"

f = open (filename)



chromosome_counts = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}


for lines in f:
    if "@" in lines:
        #to avoid the header
        pass
    if "SRR072893.17886472" in lines:
        break #I think I ended up with an erroneous .sam file - I kept getting a "list index out of range" error at the line where "chromosomes = columns[2]" because there was one line at the very end that just had SRR072893.1788 in the first column and nothing else. So I broke at the line before that (because that line had a * marked as its chromosome so it wouldn't be counted anyway) to get around the error. And I think it worked?
    else:
        columns = lines.split()
        #print lines
        chromosome = columns[2]
        
        if chromosome in chromosome_counts:
           chromosome_counts[chromosome] += 1
        else:
            pass


print chromosome_counts






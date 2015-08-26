#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

import sys


#print sys.argv

#filename =sys.argv[1]



#f = open( filename )


f = sys.stdin


name_counts={}
#Make a blank dictionary called name_counts




for line_count, data in enumerate (f):
    fields = data.split()
    gene_name=fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name] = 1
    else:
        name_counts[gene_name] += 1
        
#Iterate key, value pairs from the name counts dictionary
for key,value in name_counts.iteritems():
    print key,value
    
#The reason we would even be finding multiple numbers of different genes is that there are different transcripts for the same gene
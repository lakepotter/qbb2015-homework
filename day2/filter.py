#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open ( filename )

    #The comma after print line, here tells you to skip the next line. The default is that it will enter      a new (blank) line after the line it prints

for data in f:
    fields = data.split()
    if "tRNA" in fields[9]:
        print data,
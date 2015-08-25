#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open ( filename )

    #The comma after print line, here tells you to skip the next line. The default is that it will enter      a new (blank) line after the line it prints


#Iterate the file line by line with line_count=0

for line_count, data in enumerate (f):
    if line_count <= 10:
        pass
    elif line_count <= 15:
        print data,
    else:
        break    
    
#!/usr/bin/env python


filename = "/Users/cmdb/qbb2015-homework/day2/day2-lunch/SRR072893.sam"

f = open (filename)

line_count = 0

for lines in f:
    columns = lines.split()
    if "@" in lines:
        pass
    else:
        if line_count <= 10:
            line_count += 1
            print columns[2]
        

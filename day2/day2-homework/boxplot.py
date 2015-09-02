#!/usr/bin/env python

#Make a boxplot of the top 1/3rd, middle 1/3rd, and bottom third FPKM values in SRR072893
#HINT: .boxplot()
#HINT: remove rows where FPKM == 0

import pandas as pd
import matplotlib.pyplot as plt


#input_file = "/Users/cmdb/qbb2015/genomes/SRR072893.sam"

#FPKM - fragments of kilobase of exon per million reads mapped, found in SAM or BAM file format - which we have!

file = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")

plotdata = file[file["FPKM"]!=0]

#print plotdata

sortedplotdata=plotdata.sort("FPKM")

#index = location within an object -- maybe?

#print sortedplotdata

top = sortedplotdata[0:3183]
middle= sortedplotdata[3183:6366]
bottom=sortedplotdata[6366:9548]

#could do len() / 3 instead of hard coding 

top=top['FPKM']
middle=middle['FPKM']
bottom=bottom['FPKM']


plt.figure()
plt.title("FPKM boxplot")
plt.boxplot([top,middle,bottom])
plt.xlabel("Gene Number")
plt.ylabel("Start Position")
plt.savefig("FPKM_boxplot.png")

#could put this on a log axis so that it spreads out a bit more









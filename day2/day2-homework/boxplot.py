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

print sortedplotdata

top = sortedplotdata[0:3183]
middle= sortedplotdata[3183:6366]
bottom=sortedplotdata[6366:9548]

print top
print middle
print bottom

top.boxplot()

topplot=top.boxplot(return_type='both')
middleplot=middle.boxplot(return_type='both')
bottomplot=bottom.boxplot(return_type='both')

plt.figure()
plt.title("Top third FPKM values")
#plt.plot('both')
#plt.xlabel("X")
#plt.ylabel("Y")
plt.savefig("top third FPKM values.png")


#I'm having a hard time putting my returned values for .boxplot into plt.boxplot()






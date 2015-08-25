#!/usr/bin/env python

#Subset the lines in BDGP6.Ensembl.81.gtf that contain "Sxl". For this subset, create a plot of the start coordinates. Label your axes and add a title.
#HINT: pandas

#FBgn0264270 is Sxl

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015-homework/day1-lunch/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment='#', header=None)

df.columns=["chromosomes", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

#I want to be looking at "attributes"

print df["attributes"]

contains_Sxl=df["attributes"].str.contains("FBgn0264270")

print df[contains_Sxl]

    
plt.figure()
plt.title("Sxl")
plt.plot(df[contains_Sxl]["start"])
plt.xlabel("row number")
plt.ylabel("start position")
plt. savefig("plot_Sxl_starts.png")




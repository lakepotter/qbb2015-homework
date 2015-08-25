#!/usr/bin/env python

#Subset the lines that contain "Sxl" and are of type "transcript". Create a similar plot.
#HINT: column 3

#FBgn0264270 is Sxl

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015-homework/day1-lunch/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment='#', header=None)

df.columns=["chromosomes", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

#I want to be looking at "attributes" for the Sxl part, type for the transcript part



roi = df["type"].str.contains("transcript")
roi2 = df["attributes"].str.contains("FBgn0264270")
print df[roi][roi2]

transcript_and_contains_Sxl=df[roi][roi2]
    
plt.figure()
plt.title("Sxl transcripts")
plt.plot(transcript_and_contains_Sxl["start"])
plt.xlabel("row number")
plt.ylabel("start position")
plt. savefig("plot_Sxl_transcripts_starts.png")




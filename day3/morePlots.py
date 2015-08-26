#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

#you could just import pandas and then you would need to write something like pandas.read_file or whatever rather than pd.read_file

df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
#this is going to physically open the file

df2=pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab") #adding a new dataframe that is about females at different timestages

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

Sxl=[]
#lists have square brackets


for sample in metadata[metadata["sex"] == "female"]["sample"]:
    #the first set of brackets pulls out just the females and the second one associates the sample id with it
    #print sample
    df=pd.read_table("~/qbb2015/stringtie/"+sample+"/t_data.ctab")
    roi=df["t_name"].str.contains("FBtr0331261")
    Sxl.append(df[roi]["FPKM"].values)
        #gives us just the values from this data frame
        #want to add to the list
        
plt.figure()
plt.plot(Sxl)
plt.savefig("timecourse.png")


plt.figure()
plt.scatter(df["FPKM"],df2["FPKM"]) #when we did a boxplot, this was a list. this isn't a list - we want two seperate values for x and y
plt.xlabel("893 - male 10")
plt.ylabel("915 - female 14D")
plt.savefig("scatterplot.png")


#if we wanted to isolate that one point that is high for the female, we could make a boolean filter for y>4000 & (and use the single ampersand) x<100 and make a subset of that and then try to identify it and find out what gene that is


#how many lines correspond to various chromosomes? use a dictionary! if the first line is 2L, add 1

chromosomes_count={} 
#remember, curly braces are for dictionaries

#our table is a dataframe

for i, entry in df.iterrows(): #iterrows() makes it cycle through all of our entries. and we need it to have the i, entry because we are making a tuple?
    #print entry["chr"]
    if entry["chr"] in ["2L", "2R", "3L", "3R", "X", "Y"]:
        if entry["chr"] not in chromosomes_count:
            chromosomes_count[entry["chr"]] = 1
        else :
            chromosomes_count[entry["chr"]] += 1
        
#print chromosomes_count

#let's make a barplot for this. that seems like a good way to disply this data

#print len(chromosomes_count) #this tells you how many entries are in the dictionary - for the x axis

#print range(len(chromosomes_count))

#for the height of each bar, you want the values that are associated with the keys

#print chromosomes_count.values()
#print chromosomes_count.keys()



plt.figure()
plt.bar(left=range(len(chromosomes_count)), height=chromosomes_count.values())
plt.savefig("bar_plot")

#you can label your xticks with the chromosome names with plt.xticks
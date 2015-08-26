#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

#add stage 14 replicates to the same plot (git pull for /Users/cmdb/qbb2015/rawdata/replicates.csv)

rep_metadata = pd.read_csv("/Users/cmdb/qbb2015-homework/day3/replicates.csv")

#print rep_metadata

Sxl_f_rep=[]


for rep_f_sample in rep_metadata[rep_metadata["sex"] == "female"]["sample"]:
    rep_f_df=pd.read_table("~/qbb2015/stringtie/"+rep_f_sample+"/t_data.ctab")
    rep_f_roi=rep_f_df["t_name"].str.contains("FBtr0331261")
    Sxl_f_rep.append(rep_f_df[rep_f_roi]["FPKM"].values)
    
#print Sxl_rep

print Sxl_f_rep

Sxl_m_rep=[]

for rep_m_sample in rep_metadata[rep_metadata["sex"] == "male"]["sample"]:
    rep_m_df=pd.read_table("~/qbb2015/stringtie/"+rep_m_sample+"/t_data.ctab")
    rep_m_roi=rep_m_df["t_name"].str.contains("FBtr0331261")
    Sxl_m_rep.append(rep_m_df[rep_m_roi]["FPKM"].values)
    


    
    


#Update the timecourse.png plot of female Sxl FBtr0331261 isoform abundance
#add timecourse of male Sxl abundance to the same plot
#make it similar to pmid 21346796 Fig 3B (x-axis tick labels, color, legend, etc.)
#add stage 14 replicates to the same plot (git pull for /Users/cmdb/qbb2015/rawdata/replicates.csv)

df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
#this is going to physically open the file

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")

Sxl_f=[]
Sxl_m=[]
#lists have square brackets


for f_sample in metadata[metadata["sex"] == "female"]["sample"]:
    #the first set of brackets pulls out just the females and the second one associates the sample id with it
    #print sample
    f_df=pd.read_table("~/qbb2015/stringtie/"+f_sample+"/t_data.ctab")
    f_roi=f_df["t_name"].str.contains("FBtr0331261")
    Sxl_f.append(f_df[f_roi]["FPKM"].values)
        #gives us just the values from this data frame
        #want to add to the list
        
for m_sample in metadata[metadata["sex"] == "male"]["sample"]:
    m_df=pd.read_table("~/qbb2015/stringtie/"+m_sample+"/t_data.ctab")
    m_roi=m_df["t_name"].str.contains("FBtr0331261")
    #print roi2
    Sxl_m.append(m_df[m_roi]["FPKM"].values)
     
     
        
plt.figure()
plt.plot(Sxl_f, '-r')
plt.plot(Sxl_m, '-b')

plt.plot(4, 0, '-o', color='r')
plt.plot(5, 79.103, '-o', color='r')
plt.plot(6, 182.233, '-o', color='r')
plt.plot(7, 2.409, '-o', color='r')



plt.legend(['female', 'male'], loc='center left')
plt.xlabel('developmental stage')
plt.ylabel('mRNA abundance (RPKM)')
y_ticks=[0, 50, 100, 150, 200, 250, 300]
x_ticks=['10', '11', '12', '13', '14A', '14B', '14C', '14D']
plt.xticks( range(8), x_ticks)
plt.yticks( range(0,301,50))
plt.title('Sxl with reps')

#plt.plot(Sxl_f_rep,'-ro')


plt.savefig("replicates.png")
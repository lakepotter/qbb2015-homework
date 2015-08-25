#!/usr/bin/env python

#Load the file /Users/cmdb/qbb2015/rawdata/samples.csv. Loop through these 16 samples and load the corresponding t_data.ctab file in /Users/cmdb/qbb2015/stringtie. Print out out the row for transcript FBtr0331261.
#HINT: if samples.csv doesn't exist, cd /Users/cmdb/qbb2015 and run git pull
#HINT: .read_csv()

import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv("/Users/cmdb/qbb2015/rawdata/samples.csv")

sample_id=df["sample"]

#print sample_id    

for sample in sample_id:
    file = pd.read_table("/Users/cmdb/qbb2015/stringtie/"+sample+"/t_data.ctab")
    FBtr0331261 = file["t_name"].str.contains("FBtr0331261")
    print file[FBtr0331261]
    
    
    








#for SRR072i in CSV file 
    #roi = df["attributes"].str.contains("SRR072$i") *you might need to make some +'s?
        #but you need to make sure you're searching in the right place
        #*str() converts your data to a string

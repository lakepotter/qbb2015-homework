#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as numpy


#Create a histogram of SRR072893 FPKM values
#filter out zero-values
#log values using numpy.log





    
 
    
SRR072893_df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

#SRR072893_FPKM.append(SRR072893_df["FPKM"].values)



SRR072893_FPKM_no0 = SRR072893_df[SRR072893_df["FPKM"] != 0]

print SRR072893_FPKM_no0

#SRR072893_FPKM=SRR072893_FPKM.values

#print SRR072893_FPKM



SRR072893_FPKM_no0_log = numpy.log(SRR072893_FPKM_no0["FPKM"])

SRR072893_FPKM=[SRR072893_FPKM_no0_log]

#print SRR072893_FPKM
        
# plt.figure()
# plt.hist(SRR072893_FPKM)
#
# plt.savefig("SRR072893_FPKM_kernel_density.png")

plt.figure()
SRR072893_FPKM_no0_log.plot(kind='kde')
plt.savefig("SRR072893_FPKM_kernel_density.png")



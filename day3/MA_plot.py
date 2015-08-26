#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as numpy

#Create an MA plot

SRR072893_df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

SRR072894_df=pd.read_table("~/qbb2015/stringtie/SRR072894/t_data.ctab")




# SRR072893_FPKM = SRR072893_df[SRR072893_df["FPKM"] != 0]
# SRR072894_FPKM = SRR072894_df[SRR072894_df["FPKM"] != 0]


SRR072893_FPKM = SRR072893_df["FPKM"] != 0
SRR072894_FPKM = SRR072894_df["FPKM"] != 0

#Combine them because if there's a 0 in one column that was excluded, you don't want it to throw an error if the other one has a number and it doesn't match up

BOTH = SRR072894_FPKM & SRR072893_FPKM


comSRR072893_FPKM = SRR072893_df[BOTH]['FPKM']
comSRR072894_FPKM = SRR072894_df[BOTH]['FPKM']


# print comSRR072893_FPKM
# print comSRR072894_FPKM

logSRR3 = numpy.log(comSRR072893_FPKM)
logSRR4 = numpy.log(comSRR072894_FPKM)

Ratio = logSRR3 - logSRR4
Average = 0.5 * (logSRR3 + logSRR4)


plt.figure()
plt.plot(Average, Ratio, 'o')

plt.savefig("MA_plot_of_SRR072893_vs_SRR072894_FPKMs")


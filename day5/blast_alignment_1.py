#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as numpy
from math import log
import pylab

information = []
scores=[]
evalues=[]

for lines in open(sys.argv[1]):
    fields = lines.split()
    name = fields[0]
    ratio = fields[2]
    gaps = fields[5]
    information.append((name, ratio, gaps))
    score = fields[11]
    e_value = fields[10]
    scores.append((score))
    evalues.append((e_value))
    
    
#print scores
#print type( scores)   

#print evalues
#print type( evalues)
    
    
#print score
    
#print information
#print type( information)

print type(scores)

non_zero_scores=[]
for values in scores:
    if values != 0:
        non_zero_scores.append(values)    
print non_zero_scores
print type(non_zero_scores)
#print non_zero_scores

non_zero_evalues=[]
for values in evalues:
    if values != 0:
        non_zero_evalues.append(values)
  
print type(non_zero_evalues) 

non_zero_scores_float =[]
for numbers in non_zero_scores:
    non_zero_scores_float.append(float(numbers))
    
scores_float=[]
for numbers in scores:
    scores_float.append(float(numbers))

non_zero_evalues_float=[]
for numbers in non_zero_evalues:
    non_zero_evalues_float.append(float(numbers))
    
evalues_float=[]
for numbers in evalues:
    evalues_float.append(float(numbers))

    
print non_zero_scores_float
print type( non_zero_scores_float)

print non_zero_scores_float[3942]
    
log_scores=[]
log_scores = numpy.log(non_zero_scores_float)

log_evalues=[]
log_evalues = numpy.log(non_zero_evalues_float)


print log_scores
print type (log_scores)

print log_evalues
print type (log_evalues)

#numpy.log(non_zero_scores)
#log_evalues = numpy.log(non_zero_evalues)

#arr = numpy.array(log_score)
#list_log_score=arr.tolist()

#list_log_score=list(log_score)

#print type(log_scores)

#print log_scores


plt.figure()
plt.hist(log_scores)
plt.ylabel("log score")
plt.savefig("log_score_histogram.png")

plt.figure()
plt.hist(evalues_float)
plt.ylabel("e values")
plt.savefig("evalue_histogram.png")

#log evalues didn't seem to be very useful

plt.figure()
plt.hist(scores_float)
plt.ylabel("scores")
plt.savefig("score_histogram.png")

plt.figure()
plt.scatter(log_scores, log_evalues)
plt.xlabel("log scores")
plt.ylabel("log e values")
plt.savefig("scatter_plot.png")


    
#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys
import numpy
import copy
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles


def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        name = fields[0]
        size = int( fields[1] )
        arrays[name] = numpy.zeros( size, dtype=bool )
        #you could make your array have two dimensions arrays[name]= numpy.zeros((arraySize,3), dtype=bool)
        #but this is somewhat hard-coded for just 3 things
    return arrays
    
#Hey, look, I am making an array that is the correct size (using the reference sequence with the lengths of all of the chromosomes) with zeros in every place

def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        arrays[ chrom ][ start : end ] = 1
    return arrays
        
#Now this takes the array and updates it with values from the .bed file - whenever there is overlap, the number will change from a zero to a 1
    
# arr makes an array out of your first file (original len file)    
    
arr_SuHW = arrays_from_len_file( sys.argv[1] ) 
arr_BEAF = arrays_from_len_file( sys.argv[1] )
arr_CTCF = arrays_from_len_file( sys.argv[1] )


# set bits to file makes an array using your len_array as a base but populating it with the terms from your 2nd file

bits_SuHW = set_bits_from_file( arr_SuHW, sys.argv[2] ) 
bits_BEAF = set_bits_from_file( arr_BEAF, sys.argv[3] )
bits_CTCF = set_bits_from_file( arr_CTCF, sys.argv[4] )

#Now you will always have to have the row dm3.len DM3_Kc_SuHW.bed DM3_Kc_BEAF.bed DM3_Kc_CTCF.bed

#okay, the code works from here. Now you have three arrays that have the bit information of your three transcription factors. Now you want to compare them all three to one another.

total = 0
count_Abc = 0
count_aBc = 0
count_abC = 0
count_ABc = 0
count_aBC = 0
count_AbC = 0
count_ABC = 0

for x in [2, 3, 4]:
    for fragment in open( sys.argv[x] ):
        fields = fragment.split()
        # Parse fields
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        sl_SuHW = arr_SuHW[chrom][start:end]
        sl_BEAF = arr_BEAF[chrom][start:end]
        sl_CTCF = arr_CTCF[chrom][start:end]
    #this is a slice where you have the chromosome name, the start position, and the end position and all of the vlaues in this slice are 1 [true]
        if sl_SuHW.any() & ~sl_BEAF.any() & ~sl_CTCF.any():
            count_Abc += 1
        if sl_SuHW.any() & sl_BEAF.any() & ~sl_CTCF.any():
            count_ABc += 1
        if sl_SuHW.any() & sl_BEAF.any() & sl_CTCF.any():
            count_ABC += 1
        if ~sl_SuHW.any() & sl_BEAF.any() & ~sl_CTCF.any():
            count_aBc +=1
        if ~sl_SuHW.any() & sl_BEAF.any() & sl_CTCF.any():
            count_aBC +=1 
        if ~sl_SuHW.any() & ~sl_BEAF.any() & sl_CTCF.any(): 
            count_abC += 1
        if sl_SuHW.any() & ~sl_BEAF.any() & sl_CTCF.any(): 
            count_AbC +=1

    
    
# for fragment in open( sys.argv[3] ):
#     fields = fragment.split()
#     # Parse fields
#     chrom = fields[0]
#     start = int( fields[1] )
#     end = int( fields[2] )
#     # Get slice
#     sl_SuHW = arr_SuHW[chrom][start:end]
#     sl_BEAF = arr_BEAF[chrom][start:end]
#     sl_CTCF = arr_CTCF[chrom][start:end]
#     if sl_SuHW.any() & ~sl_BEAF.any() & ~sl_CTCF.any():
#         count_Abc += 1
#     if sl_SuHW.any() & sl_BEAF.any() & ~sl_CTCF.any():
#         count_ABc += 1
#     if sl_SuHW.any() & sl_BEAF.any() & sl_CTCF.any():
#         count_ABC += 1
#     if ~sl_SuHW.any() & sl_BEAF.any() & ~sl_CTCF.any():
#         count_aBc +=1
#     if ~sl_SuHW.any() & sl_BEAF.any() & sl_CTCF.any():
#         count_aBC +=1
#     if ~sl_SuHW.any() & ~sl_BEAF.any() & sl_CTCF.any():
#         count_abC += 1
#     if sl_SuHW.any() & ~sl_BEAF.any() & sl_CTCF.any():
#         count_AbC +=1
#
#
# for fragment in open( sys.argv[4] ):
#     fields = fragment.split()
#     # Parse fields
#     chrom = fields[0]
#     start = int( fields[1] )
#     end = int( fields[2] )
#     # Get slice
#     sl_SuHW = arr_SuHW[chrom][start:end]
#     sl_BEAF = arr_BEAF[chrom][start:end]
#     sl_CTCF = arr_CTCF[chrom][start:end]
#
#     if sl_SuHW.any() & ~sl_BEAF.any() & ~sl_CTCF.any():
#         count_Abc += 1
#     if sl_SuHW.any() & sl_BEAF.any() & ~sl_CTCF.any():
#         count_ABc += 1
#     if sl_SuHW.any() & sl_BEAF.any() & sl_CTCF.any():
#         count_ABC += 1
#     if ~sl_SuHW.any() & sl_BEAF.any() & ~sl_CTCF.any():
#         count_aBc +=1
#     if ~sl_SuHW.any() & sl_BEAF.any() & sl_CTCF.any():
#         count_aBC +=1
#     if ~sl_SuHW.any() & ~sl_BEAF.any() & sl_CTCF.any():
#         count_abC += 1
#     if sl_SuHW.any() & ~sl_BEAF.any() & sl_CTCF.any():
#         count_AbC +=1
#
# I actually made this iterable so I wouldn't have to do this code 3 times
    

print count_Abc 
print count_aBc 
print count_abC
print count_ABc
print count_aBC
print count_AbC
print count_ABC


plt.figure()
venn3(subsets = (count_Abc, count_aBc, count_ABc, count_abC, count_AbC, count_aBC, count_ABC), set_labels = ('SuHW', 'BEAF', 'CTCF'))
plt. savefig("venn_all_three.png")
    
   
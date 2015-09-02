#!/usr/bin/env python

"""
Count intersection of two BED files
"""

from __future__ import division

import sys

import chrombits


arr = chrombits.ChromosomeLocationBitArrays( fname = sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()
suhw = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )
suhw.set_bits_from_file(sys.argv[4])

ctcf.make_bed_file()
beaf.make_bed_file()
suhw.make_bed_file()

        

A_and_not_B = beaf.intersect( ctcf.complement() )

print A_and_not_B

union = ctcf.union( beaf.union( suhw ) )

print union

plt.figure()
venn3(subsets = union, set_labels = ('CTCF', 'BEAF', 'SuHW'))
plt. savefig("venn_union.png")


        
#!/usr/bin/env python

from __future__ import division
import sys
import chrombits

# Extend the chrombits package we made in class to create the set of intervals corresponding to a ChromosomeLocationsBitArrays instance
# It should return a list of 3-tuples, e.g. [ ('chr2L', 12, 400), ('chr2L', 454, 600), ... ]
# Provide a demonstration program that reads A.bed and B.bed and prints to stdout "A and not B"

arr = chrombits.ChromosomeLocationBitArrays( fname = sys.argv[1] )

CTCF = arr.copy()
BEAF = arr.copy()


CTCF.set_bits_from_file(sys.argv[2])
BEAF.set_bits_from_file(sys.argv[3])

files = CTCF.intersect(BEAF.complement())

bed_files = files.make_bed_file()

print bed_files

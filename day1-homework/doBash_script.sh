#!/bin/bash

FASTQ_DIR="/Users/cmdb/qbb2015/rawdata/SRR072893"
OUTPUT_DIR="/Users/cmdb/qbb2015/assignments/day1-homework"
GENOME="BDGP6.Ensembl.81.gtf"
GENOME_DIR="/Users/cmdb/qbb2015/genomes"
SAMPLE_PREFIX="SRR072"


for i in 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916
	do
		echo fastqc --extract -f $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -o $OUTPUT_DIR
		echo hisat -p 4 -x $GENOME_DIR/ -U $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -S $SAMPLE_PREFIX$i.sam
done

#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015-homework/day1-lunch/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment='#', header=None)

#print df

#print df.head()

#print df.describe()
    # you only get stats for col 3 and 4 because those are the only ones that are integers - the others are objects (as we see with the next command)

#print df.info()

#print df[1:5]
#print "this is what happens with df[1:5]"
#print df[0:5]
#print "this is what happens with df[0:5]"


#\n spaces things out a little bit
#print "\nthis is what happens with df[1:5]\n"


# Show rows 10 through 15 (1-based, inclusive)
# print df[9:15]

#show rows 20 through 25
#print df[19:25]

#print df.info() to get info on how we can get columns
#let's rename our columns
df.columns=["chromosomes", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]
#print df.info()


#you can sort based on column - 
#print df.sort(column="type", ascending=False)
#if you keep everything in the same order, you don't need to use the keys but if you put things in a different order (or drop things out) then you need to write the keys and say what you're defining

#print df["chromosomes"]

#subset the "chromosomes", "start", "end"

#print df[["chromosomes", "start", "end"]]
#this second set of square brackets turns it into a list

#show subset by row AND column
#print df["start"][9:15]
#print df[9:15]["start"]

#when you run the sort function, it isn't modifying the data frame. it is just doing an function and returning the new presentation.


#print df.shape #this will tell us how many rows and columns
df2=df["start"]
#print df2.shape #this also tells us how many rows and columns but now you can see that it only has one column (it says 0 but we know there's something there)

#df3=df[["start", "end"]]
#print df3.shape #you can see that it has 500,000 rows and 2 columns

df2.to_csv("startColumn.txt", sep='\t', index=False)
#okay, we are saving this as a file that can be accessed later and/or by another program. we basically just took the information that was in the earlier defined df2 and saving it elsewhere

#df means dataframe - this is where you pretty much start everything

regions_of_interest = df["start"] < 10
#we will be using this later on
#print regions_of_interest
#this way really only works for numbers

#print type(regions_of_interest)
#then you can see what kind of (file?) r_o_i is

print df[regions_of_interest]
#this prints all of the true

#remember that you can always use .shape to make sure your things are working/changing?

# ~ is the binary "not" operator in python - so whenever you want to negate a boolean, you can use that









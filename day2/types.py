#!/usr/bin/env python

#Integer
i = 10000

#Float
f = 0.333

i_as_f = float(i)
f_as_i = int(f)

#String
s = "A String"
    #Strings can have single quotes OR double quotes

#Boolean
truthy = True
falsy = False

#List
l = [1,2,3,4,5]

#Tuple
t = (1,"foo",5.0)

#What is the difference between lists and tuples? 
    #Lists are mutable - you can add and change things in them
    #Lists tend to only have one type of input (integers, strings, etc.) while Tuples can have elements       of different types - this doesn't necessarily apply to nested lists.

#Dictionary
d1 = { "key1": "value1,", "key2": "value2" }
d2 = dict( key1="value1", key2="value2" )
d3 = dict ( [ ("key1", "value1"), ("key2", "value2") ] )
    #This is really a list of tuples - the list will have however many things you want and the tuples         will only have 2 things
    #This makes things easy if you want to get your data from somewhere else?
d4 = {"key1": ["lions", "tigers", "bears"], "key2": "value2"}
    #You can have a list inside of a dictionary
    
for value in (i, f, s, truthy, l, t, d1, d2, d3) :
    print value, type ( value )
    

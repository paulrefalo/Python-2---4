#!/usr/local/bin/python3
"""Objective 6 - working with sets and dicts."""

s = set() 					# define an empty set
size = 0					# hold the size of the set s  
val = {}					# define an empty dict

while True:    
    t = input("Enter text: ")
    
    if not t:
        print("Finished")
        break  					# stops the loop
    else:   
        for w in t.split(' '):			# split on spaces and add words to the set
            s.add(w)
                      	
            if ( len(s) > size ):		# if word is new then len(s) will be bigger
                val[w] = len(s)			# set dict value
                size = len(s)			# reset size

        for word, order_discovered in val.items():	# print out the results 
            print( word, '-->', order_discovered)
            


 
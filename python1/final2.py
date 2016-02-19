#!/usr/local/bin/python3
"""Lesson 16 Obj 2 - final.py
   Read in text from a file given on the command line.  Count the frequency 
   of words of each length without punctuation and display results.
"""

import sys
import collections
import string


def len_no_punctuation(w):
        """ This function taks a string (word) as a parameter and then
            counts up just the ascii.letters for each word.  It returns the 
            number of actual letters and an integer.
        """
        n = 0						# loop over the letters and count up just the ascii_letters
        for letter in w:
            if letter in string.ascii_letters:
                n += 1
        return n
        
def graph(d, keys):
    """ This def takes a dict of the tabular data and the list of keys.
        It graphs the data as a histogram and does not return any value.
    """
    y_axis = (400, 300, 200, 100)					# y legend markers
    x_axis = max(keys)							# max values for x legend
    x_legend = '     |'							# legend formatting
    for i in range(400, -1, -20):					# loop from 400 to 0 by -20
            line = ''							# use str line to build for each line
            if ( i == 0 ):						# x-axis build
                line = '  ' + str(i) + ' ' + ('-+-' * (x_axis + 2) )
            elif ( i % 100 == 0 ):					# y-axis marker add in
                line += str(i) + ' -| '  
            else:							# otherwise just the bar
                line = '     | '
            j = 1
            for val in range(1, x_axis + 1):       			# check if x value has a paired y
                if ( d[j] >= i and i != 0 ):				# d[j] is the value or frequency
                    line += '***'					# if so add stars
                elif ( i != 0 ):
                    line += '   '					# if not add spaces
                j += 1
            print(line)
    for i in range(1, x_axis + 2 ):					# format x-axis values
         if ( i < 10 ):
             x_legend += '  ' + str(i)
         else:
             x_legend += ' ' + str(i)
    print(x_legend)
    return

if __name__ == "__main__":
     
        try:
            fn = sys.argv[1]
            f = open(fn,'r') 				# create file f the close it
        except IndexError:				# catch index problem with file
            print('A test file is required')
            sys.exit()
        except FileNotFoundError:			# catch file not found
            print('Cannot find that file')
            sys.exit()
        except Exception as msg:			# catch if something else when wrong
            print("Something unexpected occurred: {0}".format(msg))
            sys.exit()
        

        lst_of_words = list()				# declare an empty list
        lst_of_words = f.read().strip().split()		# read text into list as stripped of white space and split
        c = collections.Counter()			# form the dict c using .Counter()

        for word in lst_of_words:			# update dict c for each key
            c.update({len_no_punctuation(word):1})	# uses def to exclude punctuation in the letter count

        keylist = c.keys()				# print out the results
        print( '%8s' % 'Length', '%8s' % 'Count')
        for k, v in sorted(c.items()):			# print results of dict c
            if ( k == 0 ):				# ignore the '&' word result				
                continue
            print( '%8s' % k, '%8s' % v )
 
        print('\n')                 
        graph(c, keylist)				# graph tabular data as a histogram
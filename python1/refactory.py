#!/usr/local/bin/python3
"""Obj 16  - refractory.py"""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """

    lst_of_words = title.lower().title().split()	# create a list of words with all title case
    for i, word in enumerate(lst_of_words):		# find small_words subset NOT in position 0 and lower() 
        if word.lower() in small_words and i > 0: 
            lst_of_words[i] = word.lower()
    
    new_title = ' '.join(lst_of_words)			# join the list back together an return that list
    
    return new_title

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
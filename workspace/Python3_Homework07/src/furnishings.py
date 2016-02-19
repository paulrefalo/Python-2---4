'''
Created on Oct 18, 2015

@author: prefalo
'''

class Furnishing(object):
    '''
    Create Furnishings super class for subclassing Sofa, Bookshelf, Bed, Table
    '''
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishing):
    pass

class Bookshelf(Furnishing):
    pass

class Bed(Furnishing):
    pass

class Table(Furnishing):
    pass

def map_the_home(furniture):
    '''
    Create chart dict to hold furniture type and count for each room
    '''
    chart = {}
    for item in furniture:
        if item.room in chart:
            chart[item.room].append(item)
        else:
            chart[item.room] = [item]
    return chart

def counter(furniture):
    '''
    Create count dict to tally the furniture totals
    '''
    count = {}
    for item in furniture:
        itemClass = item.__class__.__name__
        if itemClass in count:
            count[itemClass] = count[itemClass] + 1
        else:
            count[itemClass] = 1
    for key, val in sorted(count.items()):
        print(key + ":", val)
    return count
    

if __name__ == '__main__':
    pass
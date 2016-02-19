"""
Tracking Coconuts the world around since 1910
"""

class Coconut(object):
    """
    class that allows for specific Coconut species and gives them
    the attribute of weights.  Also error checks against this list
    """
  
    def __init__(self, species):
        coconutTypes = {'South Asian': 3, 'Middle Eastern': 2.5, 'American': 3.5}
        if species in coconutTypes:
            self.weight = coconutTypes[species]
        else:
            raise KeyError("'%s' is not a valid coconut species" % (species))

class Inventory(object):
    """
    class to track the Coconut Inventory.  You can add a Coconut to the 
    Inventory list.  The total weight of the inventory is tracked.
    No removed functionality, though
    """
    
    def __init__(self):
        """
        Get a list ready for some coconuts
        """
        self.coconutInventory = []
    
    def addCoconut(self, obj):
        """
        Add a coconut to the inventory
        Check to be sure any added is instance of Coconut
        """
        if isinstance(obj, Coconut):
            self.coconutInventory.append(obj)
        else:
            raise TypeError("'%s' is not a valid coconut species" % (obj))
    
    def totalWeight(self):
        """
        Tally and return the total weight of all of our coconuts
        """
        total = 0
        for coconut in self.coconutInventory:
            total += coconut.weight
        return total
    
if __name__ == "__main__":
    Coconut('American')

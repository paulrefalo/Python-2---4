'''
Created on Nov 9, 2015

@author: prefalo
'''

class Tree:
    def __init__(self, key, value):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.value = value
        self.left = self.right = None
    def insert(self, key, value):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Tree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Tree(key, value)
        else:
            raise ValueError("Attempt to insert duplicate value")
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield (self.key, self.value)
        if self.right:
            for n in self.right.walk():
                yield n
                
    def find(self, value):
        "Find node by key and return its data"
        for k, v in self.walk():
            #print(k, v)
            if v == value:
                return (k, v)           
    
    def answer(self, value):
        (k, v) = self.find(value)
        if (k and v):
            print("The value {0} was found and is associated with the key {1}".format(v, k))
            return k
        else:
            print("No such value found")
            raise KeyError("No key associated with {0}".format(value))


if __name__ == '__main__':
    t = Tree("D", ord("D"))
    for c in "BJQKFAC":
        t.insert(c, ord(c))
        
    print(list(t.walk()))
    t.answer(70)
    t.answer(81)
    #t.answer(99) # Should fail
 


    
        
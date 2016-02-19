'''
Created on Nov 11, 2015

@author: prefalo
'''

class SubDct(dict):
    def __init__(self, default):
        self.default = default
        super().__init__()
        
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except:
            return self.default
        
    def __missing__(self, key):
        return self.default



if __name__ == '__main__':
    pass
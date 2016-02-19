'''
Created on Oct 20, 2015

@author: prefalo
'''
class Centipede():
    def __init__(self):
        '''
        Set up to lists to store info
        '''
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []
         
    def __setattr__(self, attribute, value):
        '''
        Set attribute to value and add to the legs,
        so long as attribute is not the protected 'stomach' or 'legs'
        '''
        if attribute == "stomach" or attribute == "legs":
            raise AttributeError("{0} is for internal use only".format(attribute))
        else:
            self.__dict__[attribute] = value          
            self.__dict__['legs'].append(attribute)
            
    def __call__(self, food):
        '''
        Add the item to the stomach
        '''
        self.__dict__['stomach'].append(food) 
                
    def __str__(self):
        '''
        Return csv equivalent
        '''
        return ",".join(self.__dict__['stomach'])

    def __repr__(self):
        '''
        Return csv equivalent
        '''
        return ",".join(self.__dict__['legs'])

if __name__ == '__main__':
    pass
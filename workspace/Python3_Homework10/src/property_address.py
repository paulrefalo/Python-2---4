'''
Created on Oct 20, 2015

@author: prefalo

•The custom exceptions StateError and ZipCodeError.
•Class Address that takes name, street_address, city, state, and zip_code as string arguments, which must then be set as attributes. You turn any or all of these attributes into properties in order to solve this assignment so long as they also meet these requirements: ◦After being set in __init__, the name attribute is read-only. Further attempts to modify it will trigger an AttributeError.
◦Zip code must follow the simple US pattern (nnnnn) or it throws a ZipCodeError.
◦State only allows two capital letters or it throws a StateError.

•State and Zip code validation must be done by regular expressions.
•Your project must include (and your program must pass!) the unittest test_property_address.py (listed below).

'''
import re

class Address:
    
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self.street_address = street_address
        self.city = city
        self._state = state
        self._zip_code = zip_code  
    
    '''
    Custom name property, no setter needed since no regex check, no custom exception
    '''
    @property
    def name(self):
        return self._name
    
    '''
    Custom State property
    '''
    @property
    def state(self):
        return self._state
                   
    @state.setter
    def state(self, stateValue):
        m = re.match( r'^[A-Z]{2}$', stateValue)
        if m:
            self._state = m.group()
        else:
            raise StateError("The State must be a two letter abbreviation, capitalized")
    '''
    Custom Zip Code property
    '''
    @property
    def zip_code(self):
        return self._zip_code
                  
    @zip_code.setter
    def zip_code(self, zipValue):
        matchObj = re.search( r'^\d{5}$', zipValue)
        if matchObj:
            self._zip_code = matchObj.group()
        else:
            raise ZipCodeError("The Zip Code must be of the form nnnnn")
     
'''Add in custom exception codes:  StateError and ZipCodeError'''   
class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass
        

    

    
if __name__ == '__main__':
    pass
'''
Created on Oct 20, 2015

@author: prefalo

property_address.py must append messages such as the following to a logfile named property_address.log each time test_property_address.py is run:

property_address.log:
2011-12-05 19:36:14,970 - ERROR - state - STATE exception

2011-12-05 19:36:14,970 - INFO - __init__ - Creating a new address

2011-12-05 19:36:14,986 - ERROR - zip_code - ZIPCODE exception

'''
import re
import logging
LOG_FILENAME = "address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "error" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level"
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    #log a message
    logging.info('Starting up the property address program')

class Address:
    
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self.street_address = street_address
        logging.info("Creating a new address")
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
            logging.error("STATE exception")
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
            logging.error("ZIPCODE exception")
            raise ZipCodeError("The Zip Code must be of the form nnnnn")
     
'''Add in custom exception codes:  StateError and ZipCodeError'''   
class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass
        

    

    
if __name__ == '__main__':
    pass
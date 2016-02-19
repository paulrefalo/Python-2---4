'''
Created on Oct 20, 2015

@author: prefalo

-l/--level INFO yes Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL 
-n/--name Throws a parser error if empty yes Sets the name value of the Address object 
-a/--address Throws a parser error if empty yes Sets the street_address value of the Address object 
-c/--city Throws a parser error if empty yes Sets the city value of the Address object 
-s/--state Throws a parser error if empty yes Sets the state value of the Address object 
-z/--zip_code Throws a parser error if empty yes Sets the zip_code value of the Address object 


'''
import re
import logging
import configparser
from optparse import OptionParser

config = configparser.RawConfigParser()
file = 'property_address.cfg'
config.read(file)

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')

DEFAULT_LOG_LEVEL = "info" # Default log level
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
        self._state = config.get('location', 'state')
        self._zip_code = config.get('location', 'zip_code')  
    
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
            raise StateError()
            #raise StateError("The State must be a two letter abbreviation, capitalized")
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
            raise ZipCodeError()
            #raise ZipCodeError("The Zip Code must be of the form nnnnn")
     
'''Add in custom exception codes:  StateError and ZipCodeError'''   
class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass
        

    

    
if __name__ == '__main__':
    
    # instantiate an OptionParser object
    parser = OptionParser()
    parser.add_option("-l", "--loglevel", 
                        action="store", 
                        dest="level",  
                        default="info",
                        help="Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL")
    parser.add_option("-n", "--name", 
                        action="store", 
                        dest="name",  
                        help="Sets the name value of the Address object")
    parser.add_option("-a", "--address", 
                        action="store", 
                        dest="street_address",  
                        help="Sets the street_address value of the Address object")
    parser.add_option("-c", "--city", 
                        action="store", 
                        dest="city",  
                        help="Sets the city value of the Address object")
    parser.add_option("-s", "--state", 
                        action="store", 
                        dest="state",  
                        help="Sets the state value of the Address object")
    parser.add_option("-z", "--zip_code", 
                        action="store", 
                        dest="zip_code",  
                        help="Sets the zip_code value of the Address object")
    (options, args) = parser.parse_args()
    #print("level: %s" % options.level)
    print(options)

    msg = "options -n, -a, -c, -s, -z are required"
    
    if not options.name:
        parser.error(msg)
    elif not options.street_address:
        parser.error(msg)
    elif not options.city:
        parser.error(msg)
    elif not options.state:
        parser.error(msg)
    elif not options.zip_code:
        parser.error(msg)
                   
    try:
        dataTest = Address( name=options.name, street_address=options.street_address, 
                            city=options.city, 
                            state=config.get('location', 'state'), 
                            zip_code=config.get('location', 'zip_code') )
        #dataTest.state = options.state
        #dataTest.zip_code = options.zip_code
        print(dataTest.state)
    except ZipCodeError:
        parser.error("option -z requires a valid US zip code as in xxxxx-xxxx")
    except StateError:
        parser.error("option -s requires 2 consecutive capital letters")

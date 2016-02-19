'''
Created on Oct 27, 2015

@author: prefalo
'''

import logging
import datetime
import random
import sys

LOG_FILENAME = "mathquiz.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"

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
    logging.info('Starting up the mathquiz program')

def generateNumber():
    '''
    Generate an integer from 1 to 10 inclusive
    '''
    logging.info("Generated a random integer from 1 to 10")
    return random.randint(1, 10)

def addNumbers(x, y, *args):
    '''
    Takes two integers (1-10) from generateNumber random function
    Returns user answer and the time it took to answer in seconds
    If *args, skip user input for testing purposes and give the value of arg
    to userAnswer
    '''
    logging.info("Call to addNumbers")
    
    if args:
        for arg in args:
            testAnswer = int(arg)
    else:
        testAnswer = 0
    
    
    start = datetime.datetime.now() #start
    
    if testAnswer == 0:
        try:
            print("What is the sum of {0} and {1}: ".format(x, y))
            userAnswer = int(input())
        except ValueError:
            logging.error("Bad user input; system exited")
            print("Answers must be integer and should be from 2 to 20 inclusive")
            sys.exit()
    else:
        userAnswer = int(testAnswer)
    
    end = datetime.datetime.now() #stop    
    # get times, difference, and truncate result
    answerTime = (end-start).total_seconds()
    answerTime = int(answerTime)
    
    return (userAnswer, answerTime)
    

if __name__ == '__main__':
    start_logging()
    logging.info("Starting mathquiz.py")
    answer = {}
    time = {}
    totalTime = 0
    for i in range(5):
        x = generateNumber()
        y = generateNumber()
        calcAnswer = x + y
        ( answer[i], time[i] ) = addNumbers(x, y)
        #print(answer[i], time[i])
        if answer[i] == calcAnswer:
            print("{0} is right!".format(answer[i]))
            answer[i] = "right"
        else:
            print("{0} is wrong!".format(answer[i]))
            answer[i] = "wrong"
        totalTime = totalTime + time[i]

    for i in range(5):
        print("Question #{0} took about {1} seconds to complete and was {2}".format(i+1, time[i], answer[i] ))
        
    averageTime = totalTime / 5
    print("You took {0} seconds to finish the quiz".format(totalTime))
    print("Your average time was {0} seconds per question".format(averageTime))
    logging.info("Script completed")
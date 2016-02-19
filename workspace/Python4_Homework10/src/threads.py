'''
Created on Nov 13, 2015

@author: prefalo
'''
import threading
import time
import os

def run(i, name):
    """Sleep for a given number of seconds, report and terminate."""
    print("Process {} started".format(name))
    if i == 3:
        os.chdir("..")
    time.sleep(i)
    print(name, "finished after", i, "seconds")
    print("The current directory for {0} is {1}".format(name, os.getcwd()))
    print("*" * 50)


for i in range(20):
    t = threading.Thread(target=run, args=(i, "T"+str(i)))
    t.start()

print("Threads started")


if __name__ == '__main__':
    pass
'''
control.py
Created on Nov 15, 2015

@author: prefalo
'''
import random
import string
import time
from queue import Queue
from output import OutThread
from worker import WorkerThread

start_time = time.time()
WORKERS = 10

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
#instring = input("Words of wisdom: ")
instring = ''.join(random.choice(string.ascii_uppercase) for _ in range(1000))
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()
print("Control thread terminating")

delta = time.time() - start_time
print("The script took --- %.5f seconds --- to run" % delta)

if __name__ == '__main__':
    pass

    
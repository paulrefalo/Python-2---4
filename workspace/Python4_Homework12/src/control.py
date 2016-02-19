"""
control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
"""

from multiprocessing import Queue, JoinableQueue 
from output import OutThread
from worker import WorkerThread
import random
import string

if __name__ == '__main__':

    WORKERS = 10
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    #instring = input("Words of wisdom: ")
    instring = ''.join(random.choice(string.ascii_uppercase) for _ in range(1000))
    # feed the process pool with work units
    for work in enumerate(instring):
        inq.put(work)
    # terminate the process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")

    
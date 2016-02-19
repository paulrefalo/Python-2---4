'''
Created on Nov 17, 2015

@author: prefalo
'''
import mmap
import timeit

FILENAME = "MegaTron"

def binary(chunk, limit):
    with open(FILENAME, "wb") as bf:
        offset = 0
        while offset < limit:
            bf.write(chunk * b'\0')
            offset += chunk
            
def megaMmap(chunk, limit):
    with open(FILENAME, "r+b") as f:
        m = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
        offset = 0
        while offset < limit:
            m[offset:(offset + chunk)] = b"*" * chunk
            offset += chunk
        m.close()

if __name__ == '__main__':
    for chunk in (100, 200, 500, 1000, 4096):       
        print("For chunk size:", chunk)
        bt = timeit.timeit("binary(chunk, 10000000)", 
                           "from __main__ import binary, chunk", number = 1)
        print("Binary write time: %.5f" % bt)

        mt = timeit.timeit("megaMmap(chunk, 10000000)", 
                           "from __main__ import megaMmap, chunk", number = 1)
        print("Memory map time: %.5f" % mt)
        print("*" * 50)

     
    
    
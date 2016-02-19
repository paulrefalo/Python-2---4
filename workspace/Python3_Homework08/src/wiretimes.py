'''
Created on Oct 18, 2015

@author: prefalo
'''
import struct

f = open("wireshark.bin", "rb")
# read in the global header to get past it
top = f.read(24)
globalHeader = struct.unpack('IHHiIII', top)
# print("The Global Header is", globalHeader)
    
while True:
    try:
        ts_sec, = struct.unpack('I', f.read(4))
        ts_usec, = struct.unpack('I', f.read(4))
        incl_len, = struct.unpack('I', f.read(4))
        orig_len, = struct.unpack('I', f.read(4))
        f.seek(f.tell() + incl_len)    # move to the end of the data packet
        print("This packet's timestamp is {0} sec and {1} microseconds.".format(ts_sec, ts_usec))
    except:
        f.close()
        break

if __name__ == '__main__':
    pass
'''
Created on Nov 16, 2015

@author: prefalo
'''

class sstr(str):
    def __lshift__(self, index):
        sft = self
        lResult = sft[index:] + sft[:index]
        return sstr(lResult)
    def __rshift__(self, index):
        sft = self
        rResult = sft[-index:] + sft[:-index]
        return sstr(rResult)

if __name__ == '__main__':
    test = sstr("abcde")
    for j in range(6):
        print("Shift Left", j, ":", test << j)
    print('*'*50)    
    for k in range(6):
        print("Shift Right", k, ":", test >> k)
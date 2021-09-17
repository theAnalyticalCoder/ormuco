# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:14:31 2021

@author: liam
"""

def overlap(x1,x2,x3,x4):
    '''
    if there is no overlap then ordering from least to greatest the first two elements must be
    x1,x2 or x2,x1 or x3,x4 or x4,x3
    this also assumes (1,3) (3,4) do not overlap
    it returns true if they do not overlap
    '''
    l=[x1,x2,x3,x4]
    l.sort()
    return (l[0]==min(x1,x2) and l[1]==max(x1,x2)) or (l[0]==min(x3,x4) and l[1]==max(x3,x4))
def compare(s1,s2):
    '''
    Try except handles problem of not entering a string 
    Overflow is not a problem in python so it is not handled i.e s1=100000000000000
    the function will output a negative number if s1<s2, 0 if they are equal, a postive number if s1>s2
    Once again since python is not strongly typed there will be no issue of negative Overflow i.e ints wrapping around like in Java
    '''
    try:
        f1=float(s1)
        f2=float(s2)
        return f1-f2
    except ValueError as error:
        print(error.args[0])
        
    
    
from collections import deque
class LRU():
    '''
    Every call to the LRU increases the the time by 1
    The implementation uses a queue to determine the least recently used node
    and a dictionary to store the (value,time) pair
    each call also ends with pruning the queue to see if any nodes have expired
    '''
    def __init__(self, timelimit):
        '''
        The implementation requires a Queue to keep the keys in the least recently used key is at the head
        then there is a dicitonary that contains the value of the key and the time it was used
        '''
        self.time=-1
        self.LRUdict = {}#(key,(value,time))
        self.queue=deque()#keys
        self.timelimit=timelimit
        
        
    def pruneQueue(self):
        '''
        since time increases by 1 the least recently used key could have expired
        if thats the case we delete it from the queue and from the dictionary
        
        '''
        if len(self.queue)>0:    
            key=self.queue.popleft()
            val,time=self.LRUdict[key]
            if self.time-time>self.timelimit:
                del self.LRUdict[key]
            else:
                self.queue.appendleft(key)
                
    def get(self, key):
        '''
        The program checks if the key is present in the cache 
        if so it moves the key to the back of the queue and checks if
        the head of the queue has expired
        '''
        self.time+=1
        if key not in self.LRUdict:
            #since time has increased by 1 we may have to delete the least recently used key from the queue
            self.pruneQueue()
            return -1
        #moves the key to the back of the queue because it has just been ussed
        self.queue.remove(key)
        self.queue.append(key)
        #adds the new time to the dictionart
        self.LRUdict[key]=(self.LRUdict[key][0],self.time)
        self.pruneQueue()
        
        return self.LRUdict[key][0]
    

    def put(self, key, value):
        '''
        The program updates the key,value pair if the key is present and
        adds the key to the back of the queue
        '''
        self.time+=1
        
        if key in self.LRUdict:
            self.queue.remove(key)
            self.queue.append(key)
        self.queue.append(key)
        self.LRUdict[key] = (value,self.time)
        self.pruneQueue()
        
if __name__== "__main__": 
    overlap(2,-1,2,3)
    compare("2sd","1.3")
    a=compare("1000000000000000000000000000000000000000000","1.3")
    b=compare("-1","1.3")
    L=LRU(2)
    L.put(4,5)
    L.put(1,5)
    L.get(-1)
    L.get(4)
    L.get(4)


class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        if capacity == None:
            capacity = 0
           
        self.capacity = capacity
        self.items = [None]*capacity
        self.front = 0
        self.back = 0
        self.num_items = 0 
        


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return (self.num_items == self.capacity)


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.num_items == self.capacity:
            raise IndexError
        
        self.items[self.back] = item


        if self.back == (self.capacity - 1):
            self.back = 0
        else:
            self.back = self.back + 1

        
        self.num_items = self.num_items + 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.num_items == 0:
            raise IndexError
        
        tempValue = self.items[self.front]
        self.items[self.front] = None
        
        if self.front == (self.capacity - 1):
            self.front = 0
        else:
            self.front = self.front + 1

        self.num_items = self.num_items - 1

        return tempValue



    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items


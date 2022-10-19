# Design Circular Deque
# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is    successful, or false otherwise.
#boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is     successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the         operation is successful, or false otherwise. 
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation     is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.

class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [] 
        self.k = k 
        

    def insertFront(self, value: int) -> bool:
        if len(self.deque) <self.k:
            self.deque = [value] + self.deque 
            return True 
        else:
            return False 
        
    def insertLast(self, value: int) -> bool:
        if len(self.deque) <self.k:
            self.deque =  self.deque +[value]
            return True 
        else:
            return False   

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop(0) 
            return True 
        else:
            return False 

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop() 
            return True 
        else:
            return False 

    def getFront(self) -> int:
        if len(self.deque) > 0 : 
            return self.deque[0]
        else:
            return -1 

    def getRear(self) -> int:
        if len(self.deque) > 0 : 
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0 

    def isFull(self) -> bool:
        return len(self.deque) == self.k 

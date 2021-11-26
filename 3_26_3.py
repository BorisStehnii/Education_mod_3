"""
# 1
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message.

# 2
Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message
"""

from practice_3_26_1_stack import Stack
from practice_3_26_2_queue import Queue


# 1
class StackNew(Stack):

    def __init__(self):
        super().__init__()
       
    def get_from_stack(self, item):
        res = 0
        for ind, x in enumerate(self.items):
            if x == item:
                res = self.items.pop(ind)
        if res == 0:
            raise ValueError("There is no element in this Stack")
        return res


# 2
class QueueNew(Queue):
    
    def __init__(self):
        super().__init__()

    def get_from_queue(self, item):
        res = 0
        temp = self.items
        for ind, x in enumerate(self.items):
            if x == item:
                res = self.items.pop(ind)
        if res == 0:
            raise ValueError("There is no element in this Queue")
        return res 
        

stack = StackNew()
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(5)
stack.get_from_stack(5)
print(stack.items)

queue = QueueNew()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
queue.enqueue('d')
queue.get_from_queue('b')
print(queue.items)

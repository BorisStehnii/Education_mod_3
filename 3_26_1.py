"""
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""


from practice_3_26_1_stack import Stack


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.items)

for _ in range(stack.size()):
    print(stack.pop())


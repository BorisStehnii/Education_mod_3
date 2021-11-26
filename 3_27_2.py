class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self._head = None

    def push(self, items):
        new_node = Node(items)
        temp = self._head
        new_node.next = temp
        self._head = new_node

    def pop(self):
        res = self._head
        self._head = self._head.next
        return res

    def peek(self):
        return self._head.data

    def isEmpty(self):
        return not self._head

    def size(self):
        current = self._head
        len_stack = 0
        while current:
            len_stack += 1
            current = current.next
        return len_stack

    def __repr__(self):
        temp = self._head
        res = ""
        while temp:
            res += f"{temp.data}"
            temp = temp.next
            if temp:
                res += " -> "
        return res


stack = Stack()
stack.push(3)
stack.push(5)
stack.push(7)
print(stack)
stack.pop()
print(stack)
assert stack.peek() == 5
assert stack.size() == 2
assert stack.isEmpty() == False

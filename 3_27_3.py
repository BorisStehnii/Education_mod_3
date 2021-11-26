class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self._head = None

    def push(self, items):
        new_node = Node(items)
        temp = self._head
        new_node.next = temp
        self._head = new_node

    def pop(self):
        current = self._head
        res = None
        while current:
            if not current.next.next:
                res = current.next.data
                current.next = current.next.next
                break
            current = current.next
        return res

    def peek(self):
        current = self._head
        res = None
        while current:
            if not current.next.next:
                res = current.next.data
                break
            current = current.next
        return res

    def isEmpty(self):
        return not self._head

    def size(self):
        current = self._head
        len_queue = 0
        while current:
            len_queue += 1
            current = current.next
        return len_queue

    def __repr__(self):
        temp = self._head
        res = ""
        while temp:
            res += f"{temp.data}"
            temp = temp.next
            if temp:
                res += " -> "
        return res


queue = Queue()
queue.push(3)
queue.push(5)
queue.push(7)
print(queue)
queue.pop()
print(queue)
assert queue.peek() == 5
assert queue.size() == 2
assert queue.isEmpty() == False


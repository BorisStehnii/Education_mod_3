class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self._head = None

    def posh(self, data):
        new_node = Node(data)
        current = self._head

        if not self._head:
            new_node.next = current
            self._head = new_node
            return

        while current:
            if not current.next:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def pop(self):
        current = self._head
        self._head = self._head.next
        return current

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


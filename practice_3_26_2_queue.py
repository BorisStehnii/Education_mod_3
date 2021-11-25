class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.dequeue()

    assert queue.items == ['d', 'c', 'b']
    assert queue.size() == 3
    assert queue.isEmpty() == False

    # Queue
    for _ in range(2*queue.size()):
        queue.enqueue(queue.dequeue())
        print(queue.peek())

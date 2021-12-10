from practice_3_31_2_min_bin_heap import MinBinHeap


class PriorityQueue(MinBinHeap):

    def __init__(self) -> None:
        super().__init__()
        self.list_ = self.heap_list

    def enqueue(self, val: int) -> None:
        self.insert(val)

    def dequeue(self):
        return self.pop_min()


pq = PriorityQueue()
pq.enqueue(5)
pq.enqueue(9)
pq.enqueue(6)
pq.enqueue(3)
print(pq.list_)
print(pq.dequeue())

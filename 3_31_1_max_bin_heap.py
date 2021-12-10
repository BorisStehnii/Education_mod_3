from typing import List


class MaxBinHeap:

    def __init__(self) -> None:
        self.heap_list = []
        self.current_size = -1

    def _max_child(self, i: int) -> int:
        if i * 2 + 2 > self.current_size:
            return i * 2 + 1
        if self.heap_list[i*2+1] > self.heap_list[i*2+2]:
            return i * 2 + 1
        else:
            return i * 2 + 2

    def _move_up(self, i: int) -> None:
        while (i - 1) // 2 >= 0:
            if self.heap_list[i] > self.heap_list[(i - 1) // 2]:
                self.heap_list[(i - 1) // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[(i - 1) // 2]
                i = (i - 1) // 2
            else:
                break

    def _move_down(self, i: int) -> None:
        while i * 2 + 1 <= self.current_size:
            max_c_ind = self._max_child(i)

            if self.heap_list[i] < self.heap_list[max_c_ind]:
                self.heap_list[i], self.heap_list[max_c_ind] = self.heap_list[max_c_ind], self.heap_list[i]
            else:
                break
            i = max_c_ind

    def insert(self, val) -> None:
        self.heap_list.append(val)
        self.current_size += 1
        self._move_up(self.current_size)

    def pop_max(self) -> int:
        max_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self._move_down(0)
        return max_val

    def build_heap(self, items: List[int]):
        ind = len(items)//2
        self.current_size = len(items) - 1
        self.heap_list = items[:]
        while ind >= 0:
            self._move_down(ind)
            ind -= 1


mbh = MaxBinHeap()
# mbh.insert(5)
# mbh.insert(4)
# mbh.insert(8)
# mbh.insert(9)
# mbh.insert(3)
# mbh.insert(7)
list_ = [3, 31, 5, 9, 0, 4, 5, 7]
mbh.build_heap(list_)
print(mbh.heap_list)
mbh.pop_max()
print(mbh.heap_list)

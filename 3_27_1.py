class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None

    def add(self, data):

        new_node = Node(data)

        temp = self._head
        new_node.next = temp
        self._head = new_node

    def append(self, data):
        new_node = Node(data)
        current = self._head

        while current:
            if not current.next:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def insert(self, data, ind: int = 0):

        if ind < 0:
            ind += self.size()

        if ind == 0:
            self.add(data=data)
        elif type(ind) == int and ind > self.size():
            self.append(data=data)
        elif type(ind) == int and ind > 0:
            current = self._head
            i = 0
            new_node = Node(data)
            while current:
                if i == ind-1:
                    new_node.next = current.next
                    current.next = new_node
                    break
                i += 1
                current = current.next

    def remove(self, data):
        current = self._head
        while current:
            if self._head.data == data:
                current = current.next
                self._head = current
                continue
            elif current.next and current.next.data == data:
                current.next = current.next.next
                continue
            current = current.next

    def pop(self, ind=-1):
        res = 0
        i = 0
        current = self._head
        if ind < 0:
            ind += self.size()
        while current:
            if i == ind:
                res = current.data
                self._head = self._head.next
                break
            if i == ind - 1:
                res = current.next.data
                current.next = current.next.next
                break
            i += 1
            current = current.next
        return res

    def search(self, data) -> bool:
        current = self._head

        while current:
            if current == data:
                return True
            current = current.next
        return False

    def size(self):
        len_list = 0
        current = self._head
        while current:
            len_list += 1
            current = current.next
        return len_list

    def slice(self, start, stop):
        current = self._head
        i = 0
        res_list = LinkedList()
        while current:
            if start <= i < stop:
                res_list.add(current.data)
            i += 1
            current = current.next
        return res_list

    def index(self, data):
        current = self._head
        res = None
        i = 0
        while current:
            if current.data == data:
                res = i
                break
            i += 1
            current = current.next
        return res

    def isEmpty(self):
        return not self._head

    def __repr__(self):
        temp = self._head
        res = ""
        while temp:

            res += f"{temp.data}"
            temp = temp.next
            if temp:
                res += " -> "
        return res


ll = LinkedList()
list_ = [14, 14, 14, 14, 10, 14, 14, 14, 15, "34", [2, 3], 5, 14, 14, 14, 14]
for x in list_:
    ll.add(x)
print(ll)
print(ll.slice(3, 10))

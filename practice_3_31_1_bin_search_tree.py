from pythonds.basic import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def bfs(self) -> None:
        q = Queue()
        q.enqueue(self)
        while not q.isEmpty():
            first_element = q.dequeue()
            print(first_element.value, end=' ')
            if first_element.left_child:
                q.enqueue(first_element.left_child)
            if first_element.right_child:
                q.enqueue(first_element.right_child)

    def insert_node(self, value) -> None:
        if value < self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value < self.value:
            self.left_child = self.__class__(value)
            self.left_child.parent = self
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        elif value > self.value:
            self.right_child = self.__class__(value)
            self.right_child.parent = self

    def search_btree(self, value) -> bool:
        if value < self.value and self.left_child:
            return self.left_child.search_btree(value)
        elif value > self.value and self.right_child:
            return self.right_child.search_btree(value)
        return value == self.value

    def get_min(self):      # минимальное значение для дерева
        if self.left_child:
            return self.left_child.get_min()
        return self.value

    def remove_node(self, value) -> bool:
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value)
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value)
        elif value == self.value:
            if not self.left_child and not self.right_child:    # нет детей
                if not self.parent:
                    return False
                if self == self.parent.left_child:
                    self.parent.left_child = None
                elif self == self.parent.right_child:
                    self.parent.right_child = None
                return True
            elif self.left_child and not self.right_child:      # один левый ребенок
                if self.parent:
                    if self == self.parent.left_child:
                        self.parent.left_child = self.left_child
                    elif self == self.parent.right_child:
                        self.parent.right_child = self.left_child
                else:
                    self.value = self.left_child.value
                    self.left_child.remove_node(self.value)
                return True
            elif self.right_child and not self.left_child:      # один правый ребенок
                if self.parent:
                    if self == self.parent.left_child:
                        self.parent.left_child = self.right_child
                    elif self == self.parent.right_child:
                        self.parent.right_child = self.right_child
                else:
                    self.value = self.right_child.value
                    self.right_child.remove_node(self.value)
                return True
            elif self.right_child and self.left_child:      # оба ребенка
                self.value = self.right_child.get_min()
                return self.right_child.remove_node(self.value)
        return False


bts = BinarySearchTree(1)
bts.insert_node(6)
bts.insert_node(2)
bts.insert_node(1)
bts.insert_node(3)
bts.insert_node(5)
bts.insert_node(7)
bts.bfs()
print(bts.search_btree(6))
print()
bts.remove_node(1)
bts.bfs()


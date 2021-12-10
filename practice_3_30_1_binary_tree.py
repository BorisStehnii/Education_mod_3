from pythonds.basic import Queue


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        new_node = self.__class__(value)
        new_node.left_child = self.left_child
        self.left_child = new_node
        return new_node

    def insert_right(self, value):
        new_node = self.__class__(value)
        new_node.right_child = self.right_child
        self.right_child = new_node
        return new_node

    def get_root_value(self):
        return self.value

    def set_root_value(self):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def pre_order(self):
        print(f"{self.value}", end=' ')
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(f"{self.value}", end=' ')

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(f"{self.value}", end=' ')
        if self.right_child:
            self.right_child.in_order()

    def bfs(self):
        q = Queue()
        q.enqueue(self)

        while not q.isEmpty():
            first_element = q.dequeue()
            print(first_element.value, end=' ')

            if first_element.left_child:
                q.enqueue(first_element.left_child)
            if first_element.right_child:
                q.enqueue(first_element.right_child)


root_btn = BinaryTreeNode(1)
left_1 = root_btn.insert_left(2)
right_1 = root_btn.insert_right(3)

left_left_2 = left_1.insert_left(4)
left_right_2 = left_1.insert_right(5)

right_left_2 = right_1.insert_left(6)
right_right_2 = right_1.insert_right(7)

left_left_left_3 = left_left_2.insert_left(8)
left_left_right_3 = left_left_2.insert_right(9)
print(root_btn.get_root_value())
# print(left_1.get_root_value())
root_btn.pre_order()
print()
root_btn.post_order()
print()
root_btn.in_order()
print()
root_btn.bfs()

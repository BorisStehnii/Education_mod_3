class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":

    stack = Stack()

    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.pop()

    assert stack.peek() == 5
    assert stack.items == [3, 5]
    assert stack.size() == 2
    assert stack.isEmpty() == False

    # Parentheses balanced
    stack_parentheses = Stack()
    str_ = ")(4**(3*(2+1)))"
    for i in str_:
        if i == ")" and stack_parentheses.isEmpty():
            stack_parentheses.push(i)
            break
        elif i == "(":
            stack_parentheses.push(i)
        elif i == ")":
            stack_parentheses.pop()
    print(stack_parentheses.isEmpty())


"""
Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly brackets are "balanced."
"""


from practice_3_26_1_stack import Stack


stack_parentheses = Stack()
str_ = ")(4**(3*(2+1))))"
for i in str_:
    if i == ")" and stack_parentheses.isEmpty():
        stack_parentheses.push(i)
        break
    elif i == "(":
        stack_parentheses.push(i)
    elif i == ")":
        stack_parentheses.pop()
print(stack_parentheses.isEmpty())


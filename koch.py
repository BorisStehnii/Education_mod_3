import turtle


cursor = turtle.Turtle()
cursor.pendown()


def koch_turtle(line_size, n=7):
    if n < 0:
        return
    if not n % 2:
        cursor.forward(line_size)
        cursor.right(120)
    else:
        cursor.forward(line_size)
        cursor.left(60)
    n -= 1
    koch_turtle(line_size, n)


def koch_turtle_1(line_):
    koch_turtle(line_)
    cursor.right(180)
    koch_turtle_1(line_)



koch_turtle_1(50)

input("E")

import turtle

cursor = turtle.Turtle()
cursor.pendown()


def draw_spiral(cursor_):

    for line_size in range(1000):
        cursor_.forward(line_size)
        cursor_.right(100)


draw_spiral(cursor)

input("Exit:")

import turtle


cursor = turtle.Turtle()
cursor.pendown()
cursor.speed("fastest")


def draw(l, n):
    if n == 0:
        cursor.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        cursor.forward(x)
        cursor.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        cursor.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        cursor.right(135)

    cursor.forward(x)
    cursor.left(180)
    cursor.forward(l)


def snowflake(line_size: int, n: int):
    if n == 0:
        cursor.forward(line_size)
        return

    snowflake(line_size, n-1)
    cursor.left(60)
    snowflake(line_size, n-1)
    cursor.right(120)
    snowflake(line_size, n-1)
    cursor.left(60)
    snowflake(line_size, n-1)


def koch_snowflake(line_: int, n_: int):
    line = line_/(3**n_)
    for _ in range(3):
        snowflake(line, n_)
        # cursor.left(120)
        cursor.right(120)


# draw(400, 4)

koch_snowflake(300, 2)

input("E")

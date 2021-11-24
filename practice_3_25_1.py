import turtle


class RecursiveUtils:

    def __init__(self):
        self.list_ = []
        self.number = 0
        self.n = 0
        self.i = 0
        self.honeycomb = 0

    # Перевод строки из чисел в список чисел
    def str_list(self, str_: str):

        if len(str_) == 1:
            self.list_.append(int(str_))
            return self.list_

        self.list_.append(int(str_[0]))
        self.str_list(str_[1:])
        return self.list_

    # Посчитайте факториал
    def factorial(self, num):
        if num == 1:
            return num
        return num * self.factorial(num-1)

    # - Посчитайте нули в поданной числовой строке:
    def number_zeros(self, str_: str):
        try:
            if str_[0] == "0":
                self.number += 1
            if len(str_) == 1:
                return self.number
            self.number_zeros(str_[1:])
        except TypeError:
            print("only string")
        return self.number

    def cursor_turtle(self, line_):
        cursor = turtle.Turtle()
        cursor.pendown()
        # self.move_turtle(line_, cursor_=cursor)
        self.move_honeycomb(line_, cursor_=cursor)
        # self.draw_spiral(cursor_=cursor)

    # звезда
    def move_turtle(self, line_size, cursor_):
        if line_size < 50:
            return
        cursor_.forward(line_size)
        if self.n < 4:
            cursor_.right(144)
            self.n += 1
        else:
            self.n = 0
            line_size -= 1
        self.move_turtle(line_size, cursor_)

    # соты
    def move_honeycomb(self, line_size, cursor_):

        cursor_.forward(line_size)
        if self.honeycomb == 6:
            return
        if self.n < 6:
            cursor_.right(60)
            self.n += 1
        else:
            self.n = 0
            self.honeycomb += 1
            cursor_.left(60)
        self.move_honeycomb(line_size, cursor_)

    # спираль
    def draw_spiral(self, cursor_):
        for line_size in range(1000):
            cursor.forward(line_size)
            cursor.right(100)

    # Расчёт последовательности Фибоначчи
    def fib_recursion(self, num):
        if num == 0 or num == 1:
            return num
        return self.fib_recursion(num-1) + self.fib_recursion(num-2)

    # Количество нулей в последовательности
    def number_zeros_func(self, num, i=0):
        try:
            if num % 10 == 0:
                i = 1
            if num < 10:
                return i
            num //= 10
            return i + self.number_zeros_func(num=num)
        except TypeError:
            print("only int")
        # return self.i


rec = RecursiveUtils()

# print(rec.factorial(5))
# print(rec.number_zeros("022300022"))
# rec.cursor_turtle(25)
print(rec.number_zeros_func(0))

input("Exit")

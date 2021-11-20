def fib_recursion(n):
    print(n)
    if n == 0 or n == 1:
        return n
    return fib_recursion(n-1) + fib_recursion(n-2)


def fib_nums(num):
    first_, next_ = 0, 1
    for _ in range(num):
        print(first_)
        first_, next_ = next_, next_ + first_
    return first_


def sum_natural(i):
    return i + sum_natural(i-1)


# print(fib_recursion(10))
# print(fib_nums(10))
print(sum_natural(10))
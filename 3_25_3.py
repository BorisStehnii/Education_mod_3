def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with postive integers")
    if n == 0:
        return 0
    return a + mult(a, n-1)


list_test = [0, 2, 4, 1, -1]
for i in list_test:
    print(mult(4, i))


def fibo_values(len_li):

    start, middle, end = 0, 1, 1

    while end < len_li:
        start = middle
        middle = end
        end = start + middle
    return start, middle, end


def fibonacci_search(li, len_li, value):

    if li[len_li - 1] == value:
        return len_li - 1

    start, middle, end = fibo_values(len_li)
    start_offset = -1           # смещение старта

    while end > 1:
        curr_li_ind = min(start + start_offset, len_li - 1)

        if li[curr_li_ind] < value:
            end = middle            # смещение по списку фибоначи на одно значение в перед
            middle = start
            start = end - middle

            start_offset = curr_li_ind          # обновление смещения старта

        elif li[curr_li_ind] > value:   # смещение по списку фибоначи на два значения в перед
            end = start
            middle = middle - start
            start = end - middle

        else:
            return curr_li_ind
    return False


li_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
size = len(li_)
print(fibonacci_search(li_, size, 14))

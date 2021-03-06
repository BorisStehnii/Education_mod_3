from random import randint
import time


def merge(left_list, right_list):   # слияние списков
    new_l = []
    left = right = 0
    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            new_l.append(left_list[left])
            left += 1
        else:
            new_l.append(right_list[right])
            right += 1
    while right < len(right_list):
        new_l.append(right_list[right])
        right += 1
    while left < len(left_list):
        new_l.append(left_list[left])
        left += 1
    return new_l


def merge_sort(list_):

    while len(list_) > 1:

        new_list = []
        for i in range(0, len(list_), 2):   # обращение к спискам  в списке по индексу
            if isinstance(list_[i], list):
                left_l = list_[i]
            else:
                left_l = [list_[i]]

            if i == len(list_) - 1:
                new_list.append(left_l)
                break

            if isinstance(list_[i+1], list):
                right_l = list_[i+1]
            else:
                right_l = [list_[i+1]]

            new_list.append(merge(left_l, right_l))     # добавление объединенного списка в список

        list_ = new_list    # список списков

    list_ = list_[0]
    return list_


li_1 = li_2 = [randint(0, 1000) for _ in range(200000)]
# print(li_)
start_t = time.time()
sort_li_1 = merge_sort(li_1)
print(time.time()-start_t)
# print(sort_li)
start_t = time.time()
sort_li_2 = merge_sort(li_2)
print(time.time()-start_t)

from random import randint
import time


def merge_sort(list_):
    if len(list_) == 1 or len(list_) == 0:
        return list_
    left_list, right_list = list_[:len(list_) // 2], list_[len(list_) // 2:]
    merge_sort(left_list)
    merge_sort(right_list)
    left_ind = right_ind = new_ind = 0
    new_li = [0] * (len(left_list) + len(right_list))
    while left_ind < len(left_list) and right_ind < len(right_list):
        if left_list[left_ind] <= right_list[right_ind]:
            new_li[new_ind] = left_list[left_ind]
            left_ind += 1
        else:
            new_li[new_ind] = right_list[right_ind]
            right_ind += 1
        new_ind += 1
    while left_ind < len(left_list):
        new_li[new_ind] = left_list[left_ind]
        left_ind += 1
        new_ind += 1
    while right_ind < len(right_list):
        new_li[new_ind] = right_list[right_ind]
        right_ind += 1
        new_ind += 1
    for i in range(len(list_)):
        list_[i] = new_li[i]
    return list_


li_ = [randint(0, 1000) for _ in range(200000)]
# print(li_)
start_t = time.time()
sort_li = merge_sort(li_)
print(time.time()-start_t)

# print(sort_li)

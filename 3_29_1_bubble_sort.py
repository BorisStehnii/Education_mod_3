from random import randint
import time


def bubble_double_sort(li):
    start_ind = 0

    for end_ind in range(len(li)-1, 0, -1):
        stop_ = 0
        j = end_ind
        for i in range(start_ind, end_ind):

            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                stop_ += 1

            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
                stop_ += 1
            j -= 1
        if stop_ == 0:
            break
        start_ind += 1

    return li


li_ = [randint(0, 1000) for _ in range(20000)]
# print(li_)
start_t = time.time()
sort_li = bubble_double_sort(li_)
print(time.time()-start_t)

print(sort_li)

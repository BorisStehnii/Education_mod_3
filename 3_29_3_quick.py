from random import randint
import time
import statistics


def quick_sort(list_):
    len_list = len(list_)

    if len_list <= 1:
        return list_

    median_element = statistics.median([list_[0], list_[len_list // 2], list_[len_list - 1]])
    left_list = list(filter(lambda x: x < median_element, list_))
    right_list = list(filter(lambda x: x > median_element, list_))

    return quick_sort(left_list) + [median_element] + quick_sort(right_list)


def insertion_sort(list_):

    for i in range(1, len(list_)):
        value_ind = list_[i]    # новый элемент списка
        ind = i
        while ind > 0 and list_[ind-1] > value_ind:
            list_[ind] = list_[ind-1]
            ind -= 1
        list_[ind] = value_ind

    return list_


li_ = [randint(0, 1000) for _ in range(20000)]
li_2 = li_1 = li_
# print(li_1)
start_time = time.time()
quick_sort(li_1)
print(f"quick sort {time.time() - start_time}")

# print(li_2)
start_time = time.time()
insertion_sort(li_)
print(f"insertion sort {time.time() - start_time}")

from random import randint
import time


def shell_sort(li):
    size = len(li)
    d = 1
    d_new = 1
    while d_new <= size:
        d = d_new
        d_new = d*3 + 1
    while d > 0:
        for i in range(d, size, 1):
            ival = i
            ii = i - d
            while ii >= 0 and li[ii] > li[ival]:
                li[ii], li[ival] = li[ival], li[ii]
                ival = ii
                ii = ival - d
        d //= 3

    return li


li_ = [randint(0, 1000) for _ in range(20)]
print(li_)
start_t = time.time()
sort_li = shell_sort(li_)
print(time.time()-start_t)

print(sort_li)


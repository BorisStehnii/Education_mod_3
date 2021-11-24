
def str_revers_funk(str_):
    if len(str_) == 1:
        return str_
    return str_[-1] + str_revers_funk(str_[:-1])


print(str_revers_funk("srever"))

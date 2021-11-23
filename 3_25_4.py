
def str_revers_funk(str_):
    str_revers = str_[-1]
    if len(str_) == 1:
        return str_
    return str_revers + str_revers_funk(str_[:-1])


print(str_revers_funk("srever"))

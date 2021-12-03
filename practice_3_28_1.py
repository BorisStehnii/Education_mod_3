
def binary_search(li_, len_li, item):

    start_li = 0
    end_li = len_li - 1

    while start_li <= end_li:
        ind = (end_li + start_li) // 2
        item_ind = li_[ind]
        if item_ind == item:
            return True
        elif item_ind > item:
            end_li = ind - 1

        elif item_ind < item:
            start_li = ind + 1

    return False


li = ['c', 'b', 'a', 'd', 's', 'bn', 'am', 'a', 'b', 'c', 'd']
li.sort()
size = len(li)
print(binary_search(li, size, 'm'))


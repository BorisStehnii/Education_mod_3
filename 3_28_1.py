def binary_search(li_, item, end_li, start_li=0):

    ind = (end_li + start_li) // 2
    item_ind = li_[ind]

    if item_ind == item:
        return True
    elif li_[start_li] > li_[end_li]:
        return False
    elif item_ind > item:
        end_li = ind - 1
    elif item_ind < item:
        start_li = ind + 1

    return binary_search(li_, item, end_li, start_li)


li = []
li.sort()
print(li)
size = len(li) - 1
print(binary_search(li, 'am', size))

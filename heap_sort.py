def heap_sort(my_list):
    heapify(my_list)
    list_len = len(my_list)
    
    for i in range(list_len - 1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        shift_down(my_list, 0, i - 1)

def heapify(my_list):
    list_len = len(my_list)
    for i in range(list_len):
        shift_up(my_list, i)

    return

def shift_up(my_list, i):
    if(i == 0):
        pass
    else:
        p = (i - 1) // 2
        if my_list[i] < my_list[p]:
            my_list[i], my_list[p] = my_list[p], my_list[i]
            shift_up(my_list, p)
        return

def shift_down(my_list, first, last):
    p = first
    lchild = p * 2 + 1
    rchild = p * 2 + 2
    if last < lchild:
        pass
    elif lchild <= last < rchild:
        if my_list[p] > my_list[lchild]:
            my_list[p], my_list[lchild] = my_list[lchild], my_list[p]
    else: #last >= rchild
        if my_list[p] > min(my_list[lchild], my_list[rchild]):
            if my_list[lchild] < my_list[rchild]:
                my_list[p], my_list[lchild] = my_list[lchild], my_list[p]
                shift_down(my_list, lchild, last)
            else:
                my_list[p], my_list[rchild] = my_list[rchild], my_list[p]
                shift_down(my_list, rchild, last)
    return

my_list = [5, 7, 3, 1, 0, 7, 2]
print(my_list)
heap_sort(my_list)
print(my_list)

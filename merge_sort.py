l = [1, 9, 8, 0, 1, 1, 2, 4]

def merge_sort(x):
    length = len(x)

    if(length <= 1):
        return x

    y1 = merge_sort(x[:length//2])
    y2 = merge_sort(x[length//2:])
    l1, l2 = len(y1), len(y2)
    i1 = i2 = 0
    y= []

    while i1 < l1 or i2 < l2:
        if i1 == l1:
            y.extend(y2[i2:])
            i2 = l2 #Do not miss this!
        elif i2 == l2:
            y.extend(y1[i1:])
            i1 = l1
        else:
            if y1[i1] < y2[i2]:
                y.append(y1[i1])
                i1 += 1
            else:
                y.append(y2[i2])
                i2 += 1

    return y       

print l
sorted_l = merge_sort(l)
print sorted_l

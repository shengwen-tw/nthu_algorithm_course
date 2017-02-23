l = [5, 7, 3, 1, 2,  9, 2]

def bubble_sort(l):
    length = len(l)
    for top in range(length):
        bubble = length - 1
        while bubble > top:
            if l[bubble] < l[bubble - 1]:
                tmp = l[bubble]
                l[bubble] = l[bubble - 1]
                l[bubble - 1] = tmp

            bubble -= 1

print(l)
bubble_sort(l)
print(l)

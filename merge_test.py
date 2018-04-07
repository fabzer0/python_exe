def merge(alist):
    list_size = len(alist)
    if list_size < 2:
        return alist

    print('Splitting ', alist)
    midpoint = len(alist)//2

    left_list = alist[:midpoint]
    right_list = alist[midpoint:]

    merge(left_list)
    merge(right_list)

    i = 0
    j = 0
    k = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            alist[k] = left_list[i]
            i += 1
        else:
            alist[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        alist[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        alist[k] = right_list[j]
        j += 1
        k += 1
    print('Merging ', alist)

alist = [56,23,90,45,77]
merge(alist)
print(alist)

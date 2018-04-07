def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, start, end):
    if len(alist) < 2:
        return alist
    
    if start < end:
        split_point = partition(alist, start, end)

        quick_sort_helper(alist, start, split_point-1)
        quick_sort_helper(alist, split_point+1, end)


def partition(alist, start, end):
    pivot = alist[start]
    left_mark = start + 1
    right_mark = end

    done = False
    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and alist[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
            
        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    
            temp = alist[start]
            alist[start] = alist[right_mark]
            alist[right_mark] = temp

    return right_mark

alist = [3,5,1,8,4,7,2,6]
quick_sort(alist)
print(alist)
            

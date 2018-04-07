def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint+1:], item)

alist = list(range(30))
print(binary_search_recursive(alist, 34))
print(binary_search_recursive(alist, 23))

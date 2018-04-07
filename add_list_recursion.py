def num_list(alist):
    '''this function implements adding alist of numbers using recursion
        the if statement checks to see if the length of the list is one.
        If so the integer at that position is returned. Else, we see our function
        calling itself. That implies that the num_list algorithm is recursive'''
    
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + num_list(alist[1:])

alist = list(range(1, 21))
print(num_list(alist))

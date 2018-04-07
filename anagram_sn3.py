def count_and_compare(string1, string2):
    '''this function first counts the number of times each character occurs. Since
        there are 26 possible characters, a list of 26 counters is used  one for
        each possible character. Each time we see a particular character we increment
        the counter at that position. In the end if the two lists of conters are identical
        the strings must be anagrams'''
    
    count1 = [0]*26
    count2 = [0]*26

    for i in range(len(string1)):
        pos = ord(string1[i]) - ord('a')
        count1[pos] += 1
    for i in range(len(string2)):
        pos = ord(string2[i]) - ord('a')
        count2[pos] += 1

    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if count1[j] == count2[j]:
            j += 1
        else:
            stillOk = False
    return stillOk

print(count_and_compare('apple', 'pleap'))
        

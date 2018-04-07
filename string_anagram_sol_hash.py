def string_anagram_sol_hash(astring, table_size):
    '''Since anagrams will always have the same hash value, this function is
        modified to compute different hash values in the following criteria
        94*1 + 87*2 + 43*3. The ans we get is divided by the table size to get
        the remainder as the hash value'''
    
    sum = 0
    mul = 1
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*mul
        mul += 1
    return sum % table_size

print(string_anagram_sol_hash('python', 11))
print(string_anagram_sol_hash('typhon', 11))

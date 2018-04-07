def hash(integer, table_size):
    '''This function is called a remainder method that gets the modulus of an
        integer by the size of the hash table to get the hash value'''
    
    if integer > table_size:
        return integer % table_size
    else:
        return ('Please insert a value greater than the table size')

print(hash(54, 11))
print(hash(93, 11))
print(hash(5, 11))

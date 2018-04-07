def string_hash(astring, table_size):
    sum = 0
    for i in astring:
        sum = sum + ord(i)
    return sum % table_size

print(string_hash('cat', 11))
print(string_hash('elephant', 11))
print(string_hash('typhon', 11)) # notice that anagrams will always have the same hash value
print(string_hash('python', 11)) # we are going to remedy this for anagrams to have diff values

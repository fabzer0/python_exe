def string_hash(astring, table_size):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum % table_size

print(string_hash('cat', 11))
print(string_hash('elephant', 11))

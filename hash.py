def hash(astring, table_size):
    sum = 0
    for pos in range(len(astring)):
        sum = sum+ord(astring[1])
    return sum%table_size

theList = ["car", "residents", "senior", "officer"]
hash(theList, 5)
    

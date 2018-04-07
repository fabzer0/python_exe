import time

def merge(array_main):
	half = len(array_main)//2
	
	array_1 = array_main[:half]
	array_2 = array_main[half:]
	
	array_1.sort()
	array_2.sort()
	
	len_array_1 = len(array_1)
	len_array_2 = len(array_2)
	
	index_1 = 0
	index_2 = 0
	index_main = 0
	
	while index_1 < len_array_1 and index_2 < len_array_2:
		if array_1[index_1] < array_2[index_2]:
			array_main[index_main] = array_1[index_1]
			index_1 += 1
		else:
			array_main[index_main] = array_2[index_2]
			index_2 += 1
		index_main += 1
	while index_1 < len_array_1:
		array_main[index_main] = array_1[index_1]
		index_1 += 1
		index_main += 1
	while index_2 < len_array_2:
		array_main[index_main] = array_2[index_2]
		index_2 += 1
		index_main += 1

alist = [3, 7, 4, 8, 1, 5, 2, 6]
start = time.time()
merge(alist)
end = time.time()
print(alist)
print(float(start-end))


	

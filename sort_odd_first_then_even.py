def sort(alist):
	even = []
	odd = []
	concat = []
	for i in alist:
		if i % 2 == 0:
			even.append(i)
		else:
			odd.append(i)
	for x in range(len(odd)-1, 0, -1):
		for y in range(x):
			if odd[y] > odd[y+1]:
				temp = odd[y]
				odd[y] = odd[y+1]
				odd[y+1] = temp
	for a in range(len(even)-1, 0, -1):
		for b in range(a):
			if even[b] > even[b+1]:
				temp = even[b]
				even[b] = even[b+1]
				even[b+1] = temp
	concat = odd + even
	return concat

int = [6,2,8,1,9,3,5,4,7]
print(sort(int))

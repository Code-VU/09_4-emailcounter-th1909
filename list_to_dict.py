di = {}

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

num = 0
for item in list1:
    di.update({list1[num] : list2[num]})
    num += 1

print(di)
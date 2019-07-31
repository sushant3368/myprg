# sushant pandilwar

# 31 July 2019

# # enumerate

# l = ['s','u','s','h','a','n','t']

# e = enumerate(l)

# for i in e:
# 	print(i[0],i[1])


# # zip
# numberList = [1, 2, 3]
# strList = ['one', 'two', 'three']
# strList1 = ['zero','one', 'two', 'three']

# result = zip(range(4),strList1)
# resultList = set(result)
# print(resultList)

# result = zip(numberList, strList)
# resultSet = list(result)
# print(resultSet)


# # .copy

# import copy

# old_list1 = [['a','a','a'], ['b','b','b'], ['c','c','c']]
# new_list1 = old_list1

# new_list1.append(['d','d','d'])

# print("Old list1:", old_list1)
# print("New list1:", new_list1)


# old_list2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list2 = copy.copy(old_list2)
# old_list2[1][0] = 7

# old_list2.append([4, 4, 4])

# print("\nOld list2:", old_list2)
# print("New list2:", new_list2)


# old_list3 = [['I','I','I'], ['II','II','II'], ['III','III','III']]
# new_list3 = copy.deepcopy(old_list3)
# old_list3[2][1] = 'V'

# old_list3.append(['IV','IV','IV'])

# print("\nOld list3:", old_list3)
# print("New list3:", new_list3)

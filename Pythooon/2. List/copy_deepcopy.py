from copy import deepcopy

lst1 = [10, 20, [2, 3, 4, 5, 6], 30, 40]

lst2 = lst1  # this is deepcopy

# cause id is same
lst3 = lst1.copy()
lst1.append(10)

lst4 = deepcopy(lst1)
print(lst1)
print(lst2)
print(lst3)

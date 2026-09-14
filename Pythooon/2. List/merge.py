def merge(l1,l2):
    l3=l1.extend(l2)
    print(l3)
    return l1

new=merge([1,2,3],[4,5])
print(len(new))

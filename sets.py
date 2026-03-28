#Convert a list into a set

sample_list = [1,1,2,2,2,3,3]

sample_set = set(sample_list)

print(sample_set)

#check if an element exists in the set
if 4 in sample_set:
    print("Yes")
else:
    print("No")

#Add elements

myset = set([])

myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)

#remove elements

myset.discard(5)

#SET OPERATIONS

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)

a = {1, 2, 3,4 ,5 ,6, 1, 2, 3, 4, 5, 6}
print(a)
# values are not repeated in set

b = {23, 45, 67, 78, 344, 23, 56, 56}
print()
# print(b[4])
#  indexing doesn't happen in set
print(len(b))

print()
set1 = {}
print(dir(set1))

print()
set2 = {1, 2, 3, 'A', 'B'}
# It doesn't have append
set2.add(4)
print(set2)

set2.update([1, 2, 3, 4, 5, 6, "Abhijay", "Rajvansh", "Bobby"])
print()
print(set2)

print()
set2.remove("Bobby")
print(set2)

print()
set2.pop()
print(set2)

print()
f1 = {1, 2,3 ,4 ,5, 6}
f2 = {7, 8, 9, 0, 12, 11, 1,1}
print(f1 | f2)
print(f1.union(f2))

print()
f1 = {1, 2,3 ,4 ,5, 6}
f2 = {7, 8, 9, 0, 12, 11, 1,1}
print(f1 & f2)
print(f1.intersection(f2))

print()
f1 = {1, 2,3 ,4 ,5, 6}
f2 = {7, 8, 9, 0, 12, 11, 1,1}
print(f1 - f2)
print(f1.difference(f2))

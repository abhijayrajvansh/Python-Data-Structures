a = [1, 2, 3, 5, 7, 99, 269]
print(a)

l1 = ['abhijay', 'rajvansh', 1234, '*', 45, '@']
print(l1)

print()
print("2nd element of l1 is : ", l1[1])

x = []
print(dir(x))

x = [1, 23, 56, 23, 9, 0, 0, 4, 45]
x.append(2711)
print()
print(x)

print()
x.insert(3, 6660)
# This will insert the element after 3rd position
print(x)

x.clear()
print(x)

print()
final = a + l1 + x
print(final)
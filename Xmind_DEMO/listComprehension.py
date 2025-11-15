# Method 1

list1 = [1, 2, 3, 4, 5]
list2 = []

for item in list1:
    list2.append(item ** 2)

# Method 2

list1 = [1, 2, 3, 4, 5]
list2 = [item ** 2 for item in list1]

print(list1)
print(list2)

"""
Program Output:

[1, 2, 3, 4, 5]
[1, 4, 9, 16, 25]
"""
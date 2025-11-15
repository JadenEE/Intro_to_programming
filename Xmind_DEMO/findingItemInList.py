prod_num = ['V475', 'F987', 'Q143', 'R688']

search = input("Enter a product number: ")

if search in prod_num:
    print(f"{search} was found in list")
else:
    print(f"{search} was not found in list")

"""
Program Output:

Enter a product number: A439
A439 was not found in list

Enter a product number: F987
F987 was found in list
"""
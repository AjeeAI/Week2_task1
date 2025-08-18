name_entry = input("Enter five names separated by spaces: ")
name_entry = name_entry.lower()
print(name_entry)
names = list(name_entry.split())
print(names)
names.sort()
print(names)

[print(name) for name in names]
# names = []
# name1 = input("Enter the first name: ")
# name2 = input("Enter the second name: ")
# name3 = input("Enter the third name: ")
# name4 = input("Enter the fourth name: ")
# name5 = input("Enter the fifth name: ")
# names_entry = name1 + name2 + name3 + name4 + name5
# print(names_entry) 
# names = name1, name2, name3, name4, name5
# names.lower()
# names_list = list(names)

# print(names)
# print(names_list)
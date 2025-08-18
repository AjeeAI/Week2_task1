# Using parentheses ()

# Example 1: tuple with multiple items

fruits = ("apple", "banana", "cherry")
print(fruits) # ('apple', 'banana', 'cherry')


# Without parentheses (tuple packing)

numbers = 1, 2, 3
print(numbers) #(1, 2, 3)


# Single-item tuple (must include a comma)**

single_item = ("apple",)
print(single_item) # ('apple',)
print(type(single_item))# ('apple',)

# Using the tuple() constructor

fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple) # ('apple', 'banana', 'cherry')

# Ordered

colors = ("red", "green", "blue")
print(colors[0]) # red


# Immutable ( uncomment and run. This will cause an error)
# colors[1] = "yellow"  #  TypeError

# Allow duplicates

numbers = (1, 2, 2, 3)
print(numbers) # (1, 2, 2, 3)


# Mixed data types

mixed = ("apples", 3, True, 5.6)
print(mixed) # ('apple', 3, True, 5.6)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested) # (('a', 'b'), (1, 2))

# Indexing 
fruits = ("apple", "banana", "cherry")
print(fruits[1]) # banana
print(fruits[-1]) # cherry

# Slcing 

print(fruits[0:2]) # ('apple', 'banana')
print(fruits[::-1]) # ('cherry', 'banana', 'apple')

# Concatenation

tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result) # (1, 2, 3, 4)

# Repitition
nums = (1, 2)
print(nums * 3) # (1, 2, 1, 2, 1, 2)

# Membership

fruits = ("apple", "banana", "cherry")
print("banana" in fruits) # True
print("grape" not in fruits) # True

# Iteration

for fruit in fruits:
    print(fruit)

person = ("John", 25, "Nigeria")
name, age, country = person
print(name) # John
print(age) # 25
print(country) # Nigeria

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2)) # 2  (counts occurrences of 2)
print(numbers.index(3)) # 3  (position of first occurrence of 3)

# Converting between list to tuple
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst) # [1, 2, 3, 4]

# List back to Tuple
t = tuple(lst)
print(t) # (1, 2, 3, 4)

nums = (4, 1, 7, 3)

print(len(nums)) # 4
print(max(nums)) # 7
print(min(nums)) # 1
print(sum(nums)) # 15


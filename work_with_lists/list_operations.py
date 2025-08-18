"""
Concatenation (+)**
- Joins two lists into a new list.
- Joins two lists into a new list.
"""

list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result) # [1, 2, 3, 4, 5]

"""
Repetition (*)**
- Repeats elements in a list a given number of times.
"""

nums = [1, 2]
repeated = nums * 3
print(repeated) # [1, 2, 1, 2, 1, 2]

"""Indexing**
- Access elements using their position (starting from 0).
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # apple
print(fruits[-1]) # cherry (negative index starts from the end)

"""
Slicing**
- Extract a portion of the list.
"""
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4]) # [1, 2, 3]
print(numbers[:3]) # [0, 1, 2]
print(numbers[3:]) # [3, 4, 5]
print(numbers[::2])  # [0, 2, 4] (step of 2)


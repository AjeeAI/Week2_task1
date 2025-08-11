# Question 1
# entry = input("Enter info here: ")
# print(entry.upper())

# # Question2
# entry = "python"
# print(f"The first character is {entry[0]} and the last character is {entry[-1]}")

# # Question 3
# name = input("Enter your name: ")
# print(name.replace(name, "Hello, !"))

# # Question 4
# #Thus is a function supposedly to get the length without using the len() function

# entry = "Adesoji"

# length = entry.find(entry[-1])  + 1

# print(F"The length of the entry is {length}")


# Task 5

# message = "Hello World"
# print(message.replace("World", "Python"))
"""
Task 2
"""

# Question 6
# entry = " This is a java file for checking"
# print("python" in entry)

# Question 7
entry = "Ajijolaoluwa"
print(entry[-1::-1])


# Question 8
entry = " This is my name     "

print(entry.strip())

# Question 9

sentence = input("Enter a sentence: ")
contains_a = sentence.count("a")
contains_e = sentence.count("e")
contains_i = sentence.count("i")
contains_o = sentence.count("o")
contains_u = sentence.count("u")

# Question 10
entry = "1234"
int_entry = int(entry)
print(int_entry * 2)

""" Task 3"""

# Question 11

fruits = "apple,banana,orange"
print(fruits)
print(fruits.split())

# Question 12

sentence = input("Enter a sentence: ")
word = "\n".join(sentence.split())
print(word)


# Question 13
entry = "This is a sample string"

print("_".join(entry.split()))

# Question 14

fruit = "Banana"
print(fruit.count("a"))


# Question 15
entry = "https://github.com/AjeeAI/Week2_task1.git"
print(entry.startswith("https://"))
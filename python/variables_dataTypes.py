# Variables

# Strings
name = "Harjit"

# Integers
age = 25

# Float
price = 10.99
gpa = 3.2

# Boolean
is_hacker = True

# collection = single "variable" used to store multiple values
# List = [] ordered and changeable, duplicates ok
# Set = {} unordered and immutable, but Add/Remove OK. NO dupicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# List
print("List")
fruits = ["apples", "orange", "banana", "coconut"]
for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"
fruits.append("mango")
fruits.remove("orange")
fruits.insert(0, "grapes")
print("apples" in fruits)
fruits.sort()
fruits.reverse()

for fruit in fruits:
    print(fruit)

print(fruits.index("grapes"))
print(fruits.count("grapes"))

fruits.clear()

# Set
print("Set")
fruits = {"apples", "orange", "banana", "coconut"}
print("apples" in fruits)
fruits.add("pineapple")
fruits.remove("apples")
fruits.pop()
fruits.add("pineapple")
print(fruits)

#Tuple
print("Tuple")
fruits = ("apples", "orange", "banana", "coconut", "coconut")
print(len(fruits))
print("pineapple" in fruits)
print(fruits.count("coconut"))

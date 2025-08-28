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

# 2D lists
print("2D List")

fruits =     ["apple", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for grocery in groceries:
    for item in grocery:
        print(item, end =" ")
    print()

# dictionary = collection of {key:value} pairs ordered and changeable. No duplicates.

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))
capitals.update({"Germany": "Berlin"})
capitals.pop("China")
capitals.popitem()
keys = capitals.keys()
values = capitals.values()

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

items = capitals.items()
for key,value in capitals.items():
    print(f"{key}: {value}")


#iterable = an object/ collection that can return its elements one at a time, allowing it to be iterated 
# over in a loop

#numbers = [1,2,3,4,5] # list
numbers = (1,2,3,4,5) # tuple

for number in reversed(numbers):
    print(number, end = "-")

fruits = {"apple","orange","banana", "coconut"} # sets

for fruit in fruits:
    print(fruit)

name = "Harjit Sangha" # string

for character in name:
    print(character, end=" ")

print()

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")
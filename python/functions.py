# function = a block of reusable code. Place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")

happy_birthday("Harjit", 20)
happy_birthday("Steve", 30)

# return = statement used to end a function and send a result back to the caller

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

z = add(1,2)
print(z)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("harjit", "sangha")
print(full_name)


# default arguments = a default value for certain parameters. default is used when that argument is omitted.
# make your functions more flexible, reduces # of arguments.
# 1. positional, 2. default, 3. keyword, 4. arbitrary

#default
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

import time

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

#count(30,15)

#keyword = an argument preceded by an identifier. helps with readability. order of arguments doesn't matter.

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", first = "Harjit", last = "Sangha", title= "Mr.")

for x in range(1,11):
    print(x, end = " ") # end is a keyword argument

print("1","2","3","4","5", sep = "-") # sep is also a keyword argument

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments * unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("Dr.", "Harjit", "Sangha")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(unit = "6666",
               street = "1235 street",
               city = "Detroit",
               state = "B.C",
               postal_code = "4321")

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    for key, value in kwargs.items():
        print(f"{key} : {value}")

shipping_lable("Dr.", "Harjit",
               street = "123 flore st.",
               city = "detroit",
               state = "MI",
               zip = "54321")
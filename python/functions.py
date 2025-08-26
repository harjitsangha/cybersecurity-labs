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
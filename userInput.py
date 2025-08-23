# accept user input. Returs the entered data as a string
name = input("What is your name?: ")
age = int(input("How old are you?: "))
age = age + 1
print(f"Hello {name}")
print(f"You are {age} years old")

length = int(input("What is the length of the Rectangle?: "))
width = int(input("What is the width of the Rectangle?: "))

area = length * width
print(f"Area: {area}cm²")

# Exercise: Madlibs game

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing'")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
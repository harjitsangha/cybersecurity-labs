# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("Name cannot be empty")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cannot be -ve")
#     age = int(input("Enter your age: "))

# print(f"You're {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# for loop = execute a block of code a fixed number of times

credit_card = "1234-5678-9012-3456"

for x in reversed(range(1, 11, 2)):
    print(x)

for x in credit_card:
    if(x == "-"):
        continue
    else:
        print(x)
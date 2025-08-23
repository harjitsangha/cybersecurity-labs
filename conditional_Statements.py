age = int(input("Enter your age: "))

if age >= 100:
    print("You're too old to sign up!")
elif age <= 0:
    print("You haven't been born yet!")
elif age >= 18:
    print("You're now signed up!")
else:
    print("Sorry, next year")


response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")
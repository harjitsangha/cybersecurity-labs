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

# conditional expressions: one line shortcut for the if-else statement (ternary operator)
# X if condition else Y

num = 5
a = 6
b = 7

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
# Random number guessing game
import random

low = 1
high = 100
guesses = 0

number = random.randint(low, high)
print(number)
while True:
    get_number = input(f"Enter a number between ({low} - {high}): ")
    if get_number.isdigit():
        get_number = int(get_number)
        if get_number < number:
            guesses += 1
            print(f"{get_number} is too small")
        elif get_number > number:
            guesses += 1
            print(f"{get_number} is too high")
        else:
            guesses += 1
            print("You won!")
            break
    else:
        print("Invalid guess")
print(f"Number of guesses: {guesses}")
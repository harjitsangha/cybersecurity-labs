# if __name__ == _main_: (this script can be imported or run standalone)
# functions and classes in this module can be reused without the main block of code executing
# good practice (code is modular, helps readability, leaves no global variables, avoid unintended execution)
# ex" library = import library for functionality. when running library directly, display a help page.

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is dunder")
    favorite_food("pizza")
    print("Good bye!")

if __name__ == '__main__':
    main()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+ - * /): ")

if(operator == "+"):
    print(round((num1 + num2), 3))
elif(operator == "-"):
    print(round((num1 - num2), 3))
elif(operator == "*"):
    print(round((num1 * num2), 3)) 
elif(operator == "/"):
    print(round((num1 / num2), 3))  
else:
    print(f"{operator} is not a valid operator")


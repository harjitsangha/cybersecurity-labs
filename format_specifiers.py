# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 1500.56555

print(f"Price 1 is ${price1:+.2f}") # two decimal points
print(f"Price 2 is ${price2:+010}")  # value will have 10 spaces
print(f"Price 3 is ${price3:<10}") # right justified
print(f"Price 4 is ${price4:^10}") # center align
print(f"Price 1 is ${price1:+}") # +ve values preceded with + sign
print(f"Price 4 is ${price4:+,.2f}") # each thousand's place is separated with a ,

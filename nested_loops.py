# nested loop = a loop within another loop (outer, inner)
#               out loop:
#                    inner loop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()
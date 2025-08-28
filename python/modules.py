# module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

#import math
import example

result = example.pi
result1 = example.square(3)
result2 = example.cube(3)
result3 = example.circumference(3)
result4 = example.area(3)

print(result)
print(result1)
print(result2)
print(f"{result3:.2f}")
print(result4)

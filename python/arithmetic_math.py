import math
friends = 4

friends += 1 # add
print(friends)
friends -= 2 # subtract
print(friends)
friends *= 2 # multiply
print(friends)
friends /= 2 # divide
print(friends)
friends **= 2 # exponent
print(friends)
friends %= 2 # modulas (remainder of any division)
print(friends)

x = 2.5
y = 4
z = 25

result = round(x) # round to the nearest whole integer
print(result) 
result = abs(y) # find absolute value of an integer distance away from 0 as a whole number
print(result)
result = pow(y,3) # multiply base to a given power
print(result)
result = max(x,y,z)
print(result)
result = min(x,y,z)
print(result)
result = math.sqrt(z)
print(result)
result = math.ceil(x)
print(result)
result = math.floor(x)
print(result)

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {round(circumference, 2)}cm")
area = math.pi * pow(radius,2)
print(f"Area of the circle is {round(area, 2)}cm²")

a = float(input("Enter side A of the triangle: "))
b = float(input("Enter side B of the triangle: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The side C of the triangle is: {round(c, 2)}")
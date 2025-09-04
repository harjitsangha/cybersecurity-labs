# object = a "bundle" of related attributes (variables) and methods (functioms)
#           You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

from car import Car


car1 = Car("Mustang", "2025", "Red", False)
car2 = Car("Corvette", "2025", "blue", True)

car1.describe()
car1.drive()
car1.stop()
car2.describe()
car2.drive()
car2.stop()

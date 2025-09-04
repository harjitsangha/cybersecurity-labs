# class variables = shared among all instances of a class
#                   defined outside the constructor
#                   allow you to share data among all objects created from that class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
    
student1  = Student("Harjit" , 60)
student2 = Student("Spongebob", 30)

print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_students)

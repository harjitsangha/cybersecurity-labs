# class methods = allow operations related to the class itself
# take (cls) as the first parameter, which represents the class itself.

# instance methods = best for operations on instances of the class (objects)
# static methods = best for utility functions that do not need access to class data
# class methods = best for class-level data or require access to the class itself

class Student:

    count = 0
    totalgpa= 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.totalgpa += gpa
    
    #instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"


    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.totalgpa / cls.count: .2f}"


student1 = Student("Jack", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)   
print(Student.get_count())
print(Student.get_average_gpa())
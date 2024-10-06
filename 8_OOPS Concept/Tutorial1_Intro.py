#OOP

"""
To map with real world scenarious ,
we started using objects in code

This is called object oriented programming


"""

#create class
# class Student1:
#     name = "Karan"


# #creating objects/instances of class

# s1 = Student1()
# print(s1)
# print(s1.name)

# s2 = Student1()
# print(s2)
# print(s2.name)


# class Car:
#     color = "Blue"


# car1 = Car()
# print(car1.color)

#class is collection of 2 things 
#Attributes(data)
#Methods(Functions)

#Constructor

class Student():

    college_name ="XYZ College"
    #self -- new object reference
    #constructor is invoked automatically
    name = "anonymous"

    #default constructor
    def __init__(self) -> None:
        pass

    #parametrized constructor
    def __init__(self,name,marks) -> None:
        self.name =name #obj attr > class attr
        self.marks = marks
        print("Adding new student in Database")
    
    def hello(self):
        print("Hello, Welocme here", self.name)

s1 = Student("Karan",90)
print(s1)
print(s1.name,s1.marks) #karan
s1.hello()


s2 =Student("Ram",34)
print(s2.name,s2.marks)


# Attributes
# Class & Instance attributes

print(Student.college_name)

print(s2.college_name)


#WAP to create student class and take marks of three subjects as arguments in constructor
#Create a method to print the average


class Student_Marks:
    def __init__(self,name,marks) -> None:
        self.name =name
        self.marks = marks
        
    def get_avg(self):
        sum=0
        for item in self.marks:
            sum += item
        print(f"Hi, {self.name} :Your avg score is : {sum/3}")
        
   


s1 = Student_Marks("Tony",[99,90,88])
#print(s1.get_avg())
s1.get_avg()















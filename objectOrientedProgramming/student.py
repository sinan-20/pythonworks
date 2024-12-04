# Student[name,rollnumber,age,course]

class Student:

    name:str

    rollnumber:int

    age:int

    course:str

    def set_student(self,name,rollnumber,age,course):

        self.name=name

        self.rollnumber=rollnumber

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.rollnumber,self.age,self.course)

students_instance1=Student()

students_instance1.set_student("sinan",3,25,"django")
students_instance1.display()

     

# initialize attributes(instance variable)
# constructor

# initializing instance variable constructor

# python   __init__

# do not call seprate constructor
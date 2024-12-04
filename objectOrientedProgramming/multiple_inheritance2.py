class Person:

    name:str

    age:int

    def __init__(self,name,age):

        self.name=name

        self.age=age

    # def __str__(self):

        # return self.name
    
    def display_person_info(self):

        print(self.name,self.age)


class Employee:

    emp_id:int

    salary:int

    def __init__(self,emp_id,salary):

        self.emp_id=emp_id

        self.salary=salary

    def display_employee_info(self):

        print(self.emp_id,self.salary)

class Manager(Person,Employee):

    department:str

    def __init__(self,name,age,emp_id,salary,department):

        Person.__init__(self,name,age)

        Employee.__init__(self,emp_id,salary)

        self.department=department

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()

        print(self.department)
manager__instance=Manager("sinan",21,101,32000,"HR")

manager__instance.display_manager_info()
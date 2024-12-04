

class Employee:

    eid:int

    name:str

    department:str

    salary:int


    def set_employee(self,eid,name,department,salary):

        self.eid=eid

        self.name=name

        self.department=department

        self.salary=salary

    def disply(self):

        print(self.eid,self.name,self.department,self.salary)

employee_instance1=Employee()

employee_instance1.set_employee(101,"sinan","HR",35000)

employee_instance1.disply()
#method_overloading(same method name defrend number of parameters)

class Operation:

    def add(self,num1,num2):

        print(num1+num2)#this method is doesnt work bcouse python is a interpreted language,python does not work method overloading

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

obj=Operation()
obj.add(10,20,30)

obj.add(101,121)
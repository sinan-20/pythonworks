# initialize attributes(instance variable)
# constructor

# initializing instance variable constructor

# python   __init__

# do not call seprate constructor




class Mobile:

    name:str

    price:int

    brand:str

    def __init__(self,name,price,brand):

        self.name=name

        self.price=price

        self.brand=brand

    def display(self):

        print(self.name,self.price,self.brand)

mobile_instance=Mobile("Huewei7A",13000,"Huewei")
    
mobile_instance.display()

     
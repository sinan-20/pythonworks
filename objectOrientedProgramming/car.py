

class Car:

    name:str

    brand:str

    fuel_type:str

    def __init__(self,name,brand,fuel_type):

        self.name=name

        self.brand=brand

        self.fuel_type=fuel_type

    def disply(self):

        print(self.name,self.brand,self.fuel_type)

    def __str__(self):

        return self.name

car_instance1=Car("swift","suzuki","petrol")
car_instance1.disply()

print(car_instance1)
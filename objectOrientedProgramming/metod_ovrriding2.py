class Shipping:


    def calculate_shipping_cost(self,weight):

        print(weight*5)

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        print(weight*20)

class StandardShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        print(weight*10)


ExpressShipping_instance=ExpressShipping()
ExpressShipping_instance.calculate_shipping_cost(10)

StandardShipping_instance=StandardShipping()
StandardShipping_instance.calculate_shipping_cost(10)




# polymorphism(more than many forms)
    # method overloading()



# class
# object
# _init_
# super()
# self
# inheritance
    # single
    # multilevel
    # multiple
# polymorphism
    # method overloading
    # meothod_overriding
# Abstraction
    # hiding implimentation details

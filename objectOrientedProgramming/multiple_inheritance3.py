class Cusine:

    cusine_name:str

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

    def disply_cusine_info(self):

        print(self.cusine_name)

class MealType:

    meal_type:str

    def __init__(self,meal_type):

        self.meal_type=meal_type

    def disply_meal_type(self):

        print(self.meal_type)
    
class Dish(Cusine,MealType):

    dish_name:str

    def __init__(self,cusine_name,meal_type,dish_name):

        Cusine.__init__(self,cusine_name)

        MealType.__init__(self,meal_type)

        self.dish_name=dish_name

    def display_dish_info(self):

        self.disply_cusine_info()
        self.disply_meal_type()

        print(self.dish_name)

dish_instance=Dish("ITALIAN","BREAK FAST","ITALIAN PASTA")

dish_instance.display_dish_info()
        



        

class Animal:

    name:str

    spiecies:str

    def __init__(self,name,spiecies):

        self.name=name

        self.spiecies=spiecies

    def __str__(self):

        return self.name
    
class Lion(Animal):

    def __init__(self,name,spiecies):
        super().__init__(name,spiecies)

    def sound(self):
        print("Ggggggrrrrrrrrrrrrrrrrrrrrr")

lion_instance=Lion("Lion","carnivorous")

print(lion_instance)

print(lion_instance.sound())

class Cat(Animal):
    def __init__(self, name, spiecies):
        super().__init__(name, spiecies)

    def sound(self):
        print("meaooowwwwwwww")

cat_instance=Cat("cat","hgggdff")

print(cat_instance)
print(cat_instance.sound())


    
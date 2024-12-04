class person:

    name:str

    age:int

    def __init__(self,name,age):

        self.name=name

        self.age=age


    @property
    def get_age(self):

        print(self.age)

    
    @property #if we want to convert method to attribute 
    def get_name(self):

        print(self.name)

person_instance=person("sinan",21)

person_instance.get_age

person_instance.get_name
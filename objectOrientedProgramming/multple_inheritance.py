

class GrandParent:

    def m1(self):
        print("grand parent class m1 method")

class Parent:

    def m2(self):
        print("parent class m2 metod")


class Chlid(Parent,GrandParent):

    def m3(self):
        print("child class m3 method")

child_inheritance=Chlid()
child_inheritance.m1()
child_inheritance.m2()
child_inheritance.m3()

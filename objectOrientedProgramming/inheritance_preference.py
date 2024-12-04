class GrandParent:

    def m(self):
        print("grand parent class m method")

class Parent:

    def m(self):
        print("parent class m metod")


class Chlid(Parent,GrandParent):

    def m3(self):
        print("child class m3 method")

child_inheritance=Chlid()
child_inheritance.m3()
child_inheritance.m()

# here both parent & grandparent define (m) so python handle inherit orderwise


class Editor:

    name:str

    vendor:str

    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    # def disply(self):
        # print(self.name,self.vendor)
    
    def __str__(self):

        return self.name
    
editor_instance1=Editor("pycharm","jebrains")
editor_instance2=Editor("intellij","jetbrains")
editor_instance3=Editor("vscode","microsoft")

print(editor_instance2)

# editor_instance2.disply()


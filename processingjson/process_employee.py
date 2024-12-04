from json import load

f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\employee.json")

data=load(f)

for emp in data:

    print(emp)
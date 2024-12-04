# create reference file

f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\friuts.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)
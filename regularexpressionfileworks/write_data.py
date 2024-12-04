from re import findall

f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\regularexpressionfileworks\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

data=findall(pattern,content)

for date in data:

    print(date) 
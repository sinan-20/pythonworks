from re import findall

f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\regularexpressionfileworks\\https_files.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)
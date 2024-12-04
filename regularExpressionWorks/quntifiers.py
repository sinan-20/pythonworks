

from re import finditer

text="abababbaababaabbaaaabba"

# pattern="a{2}"
pattern="a{1,3}" #minimum 1 maximum 3

matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())
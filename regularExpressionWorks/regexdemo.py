
from re import finditer

text="fat cat runs very fast to catch the rat"

matcher=finditer("at",text)

for obj in matcher:
    print(obj.start(),obj.group())



# text="I have 3 cars,2 bikes and 1 Cycle"

# digits=


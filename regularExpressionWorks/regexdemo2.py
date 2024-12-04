
from re import finditer

text="I have 3 cars,2 bikes and 1 Cycle"

# pattern="[a-z]"#chk for all lower case alphebets
# pattern="[A-Z]"#chk for all upper cae alphebets
# pattern="[a-zA-Z]"#chk for all alphebets
# pattern="[0-9]"#chk for all numbers
# pattern="[a-zA-Z0-9]"#chk for all alphanumerics
# pattern="[^ak]"#excude a,k


# all lower case ailphabets exclude a,k
# pattern="[^akA-Z0-9,\- ]"


# all special characers
pattern="[^a-zA-Z0-9]"


matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())

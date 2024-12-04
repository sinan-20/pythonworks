from re import fullmatch

user_input=input("enter varialble name:")

# startng with an alphebet(lower case,upper case)
# any number of alphabets,digits,_

pattern="[a-zA-Z][a-zA-Z0-9]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")

else:
    print("valid")
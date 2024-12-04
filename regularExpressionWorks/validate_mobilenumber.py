

# rule 10 digit
# validate mobile number

from re import fullmatch

user_input=input("enter mobile number:")

pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")

else:
    print("valid")
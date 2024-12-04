from re import fullmatch
user_input=input("enter variable name:")

# starting with an alphebet from p-t
# in second place mustbe a number thst is / by 3
# followed by any number aphabeats,numbers,@

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invalid")

else:
    print("valid")

from re import fullmatch

vehcle_reg_num=input("enter vehicle registration number:")

# starting with KL
# 2 digits
# alphebets minimum 1 maximum 2
# 4 digits

pattern="(KL)+[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,vehcle_reg_num)

if matcher==None:
    print("invalid")

else:
    print("valid")


# passport
# adhar number
# drivig licence
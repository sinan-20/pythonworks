num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

if num1>num2 and num1>num3:
    if num2>num3:
        print(f"sorted {num1,num2,num3}")

    else:
        print(f"sorted {num1,num3,num2}")

    

elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"sorted {num2,num1,num3}")
    else:
        print(f"sorted {num2,num3,num1}")

    

elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"sorted {num3,num1,num3}")
    else:
        print(f"sorted {num2,num3,num1}")
   

# elif num1==num2 and num1==num3:
#     print("three numbers are equal")

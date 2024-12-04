
num1=(int(input("enter a number")))
num2=(int(input("enter a number")))
num3=(int(input("enter a number")))

if num1>num2 and num1<num3:
    print(f" secod largest {num1}")

elif num2>num1 and num2<num3:
    print(f"second largest {num2}")

elif num3>num1 and num3<num2:
    print(f"second largest {num3}")

elif num1==num2 and num1==num3:
    print("three numbers are equal")
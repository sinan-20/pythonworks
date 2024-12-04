

num=int(input("enter number:"))#6

total=0

for i in range(1,num):#1 to 5

    if num%i==0:#6%1==0

        total=total+i

print("perfect number" if total==num else "not perfect number")
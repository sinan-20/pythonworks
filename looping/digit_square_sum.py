

number=int(input("enter the number"))#123 ,12


total=0

while(number!=0):#123!=0

    digit=number%10#123%10=3
    

    square=digit**2# 3**2=9

    total=total+square# 0+9=9

    number=number//10 #123//10=12

print(total)
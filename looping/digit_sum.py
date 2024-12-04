

number=int(input("enter the number:"))#123

total=0

while(number!=0):#123!=0

    digit=number%10#123%10=3

    total=total+digit#0+3=3

    number=number//10

print(total)

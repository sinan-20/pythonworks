

number=int(input("enter the number:"))#123

original=number

digit_count=len(str(number))#3

total=0

while(number!=0):#123!=0

    digit=number%10#123%10=3

    exponent=digit**digit_count#3**3=27

    total=total+exponent#0+27

    number=number//10#123//10=12


print("amstrong number" if original==total else "not amstrong number")




num1=int(input("enter number"))#4
num2=int(input("enter the number"))#6

max_num=max(num1,num2)#6

for i in range(max_num,(num1*num2)+1,max_num):#(6,24,6)

    if i%num1==0 and i%num2==0:

        print(i)

        break
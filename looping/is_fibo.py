

number=int(input("enter number"))

prev=0

current=1

is_fibo=False


for i in range(1,number+1):#1 to 7

    next=prev+current #0+1

    prev=current#preve=1

    current=next#current=2

    if next==number:#2==6

        is_fibo=True

        break

print(is_fibo)
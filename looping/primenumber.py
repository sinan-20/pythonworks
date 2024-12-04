


number=int(input("enter the number:"))#4

is_prime=True

for i in range(2,number):#i=2,3,4

    if number%i==0:

        is_prime=False

        break

print(is_prime)


def is_prime(num):

    num_is_prime=True

    for i in range(2,num):

        if num%i==0:

            num_is_prime=False

    print(num_is_prime)

is_prime(5)





        

        

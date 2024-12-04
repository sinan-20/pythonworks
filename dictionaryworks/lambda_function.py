

# add two numbers using normal function


def add(n1,n2):

    return n1+n2

print(add(4,5))


# using lamda function for adding two numbers

add=lambda num1,num2:num1+num2

print(add(6,5))


# lambda function for subtracting two numbers

sub=lambda number1,numbwr2:number1-numbwr2

print(sub(10,4))


# find cube using lambda function

cube=lambda num:num**3

print(cube(4))

# print max length string


max_two=lambda str1,str2:str1 if len(str1) > len(str2) else str2

print(max_two("sinan","sinu"))




# min length str

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("sinan","sinu"))


# print smart sub

smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1

print(smart_sub(21,11))





words=["hello","hai","morning","test","apple"]

def get_length(word):

    return len(word)

print(max(words,key=get_length))

#  using lambda function

get_legth=lambda word:len(word)

print(max(words,key=get_length))
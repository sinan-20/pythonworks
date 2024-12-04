
def add_numbers(*args):

    return sum(args)

print(add_numbers(10,21,34))

print(add_numbers(122,3,4,3,5))

print(add_numbers(12,34,55,66,34,21,23,3))



# create a function that accept any number of arguments and returns second maximum number

def second_largest(*args):

    sorted_elements=sorted(args, reverse=True)

    return sorted_elements[1]

print(second_largest(12,32,34,31))


# *args any number of arguments


def disply_mobile_data(**kwargs):

    print(kwargs.get("name"))
    print(kwargs.get("price"))

disply_mobile_data(name="Huwei",price=13000,model="Huweiy7a")


def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)
    
    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result*=num

        return result
    
print(calculator(10,20,30,operation="*"))

print(calculator(10,20,30,operation="+"))


def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)
    
    if kwargs.get("operation")=="total":

        return sum(args)
    
print(student_info(10,11,12,8,9,operation="total"))
print(student_info(10,11,12,8,9,operation="avg"))

def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")==True:

        return sorted(args,reverse=True)
    
    if kwargs.get("reverse")==False:

        return sorted(args,reverse=False)
    
print(sort_numbers(21,12,54,32,56,reverse=True))
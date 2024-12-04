

arr=[100,200,300,400,500]

k=int(input("enter k:"))


for i in range(1,k+1):

    popped_element=arr.pop()

    arr.insert(0,popped_element)

print(arr)

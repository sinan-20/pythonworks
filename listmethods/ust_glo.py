

arr=[100,200,300,400,500,600,700,800,900]


odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0 ]


for i in range(1,len(arr),2):

    elemnets=odd_position_elements.pop()

    arr[i]=elemnets

print(arr)


# -----------------------------------------------------------------------------------

#                                 another method



arr=[100,200,300,400,500,600,700,800,900]

left=1

right=len(arr)-1

if right%2==0:

    right-=1

while (left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)
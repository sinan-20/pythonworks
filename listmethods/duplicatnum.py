

arr=[1,2,2,2,1,7,8,4,5,6,4,5]

arr.sort()

duplicate_numbers=[]

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[i]-arr[j]

    if result==0:

        if arr[i] not in duplicate_numbers:

            duplicate_numbers.append(arr[i])

print(duplicate_numbers)
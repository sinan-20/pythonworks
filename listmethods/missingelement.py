
arr=[1,2,6,4,3]

# n=5

# count_sum=sum(range(n+1))

# sumofgivennumber=sum(arr)

# missing_num=count_sum-sumofgivennumber

# print(missing_num)






arr.sort()

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result!=1:

        print(arr[i]+1 ,"is missing")

        break
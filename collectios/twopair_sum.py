

arr=[2,3,4,5]

sum=int(input("enter a number:"))

# for i in range(0,len(arr)-1):

#     for j in range(i+1,len(arr)):

#         current_sum=arr[i]+arr[j]

#         if sum==current_sum:

#             print(arr[i],arr[j])

            # break


#   _______________________________________________________
# 
#        that prgrm is high complexity 
# 
#     another way of that prgrm
#    

        

left=0

right=len(arr)-1

while(left<right):

    cur_sum= arr[left]+arr[right]

    if cur_sum==sum:

        print(arr[left],arr[right])

        break

    elif cur_sum<sum:

        left+=1

    elif cur_sum>sum:

        right-=1


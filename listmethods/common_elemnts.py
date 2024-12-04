

arr1=[10,13,8,11,20]
arr2=[2,20,8,7,13]


# for i in range(len(arr1)):
#     for j in range(len(arr2)):

#         if arr1[i]==arr2[j]:

#             print(arr1[i])



# this methord is complicated 


#----------------------------------------------------

# another methord


arr1.sort()
arr2.sort()

p1=0
p2=0

while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        # print(arr1[p1])

        p1+=1
        p2+=1

    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr1[p1]>arr2[p2]:

        p2+=1



arr3=[32,4,1,2,45]
arr4=[1,32,45,76]

arr3.sort()
arr4.sort()

p3=0

p4=0

while(p3<len(arr3) and p4<len(arr4)):

    if arr3[p3]==arr4[p4]:

        print(arr3[p3])

        p3+=1

        p4+=1

    elif arr3[p3]>arr4[p4]:

        p4+=1

    elif arr4[p4]>arr3[p3]:
        p3+=1
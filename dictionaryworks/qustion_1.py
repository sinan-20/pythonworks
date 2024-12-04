

arr=[10,20,30,40,2,3]

# {10:100,20:400,30:900,40:1600,2:4,3:9}

# result={}

# for num in arr:

#     square=num**2

#     result[num]=square

# print(result)


result={num:num**2 for num in arr}
print(result)
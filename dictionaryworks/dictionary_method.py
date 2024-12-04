# employee id,name,department,age,salary

employee={"id":101,"name":"sinan","department":"developer","age":21,"salary":25000}


print(employee.get("department"))#get(key)

employee.pop("salary")#pop(key)
print(employee)

for k in employee.keys():#return all keys => keys()
    print(k)

print("----------------------------------------------------")

for v in employee.values():#return all keys => values()

    print(v)

print("--------------------------------------")

for k,v in employee.items():#return keys and values
    print(k,v)



# method--------------------------------------


# get(key)

# pop(key)

# keys() return all keys

# values() return all values

# items() return keys and values
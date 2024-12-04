

arr=[11,20,33,40,11,20]

# syntax of dictionary comprehansion  => result={key:values iteration condition}

result={num:num**3 for num in arr }

print(result)

even_squere={num:num**2 for num in arr if num%2==0}

odd_cubes={ num:num**3 for num in arr if num%2!=0}

print("evn sqre",even_squere)

print("odd cubes",odd_cubes)


frequency_count={num:arr.count(num) for num in arr }
print(frequency_count)



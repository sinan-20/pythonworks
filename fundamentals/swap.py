

num1=100
num2=200

print(f"values b4 swapping num1={num1},num2{num2}")

#logic1

# temp=num1
# num1=num2
# num2=temp

# logic2

num1=num1+num2 # 100+200=300
num2=num1-num2 # 300-200=100
num1=num1-num2 # 300-100=200
print(f"value of after swapping num1={num1},num2={num2}")



# create dictionary employee with keys eid,name,salary,dapartment,experience


employee={"eid":101,"name":"sinan","salary":20000,"department":"HR","experience":6}

print(employee)


# add contact number

employee["contact"]=9778767654

print(employee)

# if experience >5 update employee salary as current salary +10000  else current salary +5000


if employee["experience"]>5:

    employee["salary"]+=10000

else :

    employee["salary"]+=5000

print(employee)

# add role as SDE if experience >5 else add role JDE

if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)


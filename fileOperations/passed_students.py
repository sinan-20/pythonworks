f1=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\allstudents.txt")
f2=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\failed_students.txt")


all_students_lst=set()

failed_student=set()

for line in f1:

    line=line.rstrip("\n")

    all_students_lst.add(line)

for line in f2:
    line=line.rstrip("\n")

    failed_student.add(line)

passed_students=all_students_lst.difference(failed_student)

print(passed_students)

f1.close()
f2.close()


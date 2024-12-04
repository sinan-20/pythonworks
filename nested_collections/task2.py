

student_data={
    "hari":[45,40,35],
    "vipin":[34,40,35],
    "vinay":[46,35,35],
    "bijoy":[34,36,35],
    "anvin":[38,45,35]
}

# index=3

# for i,element in enumerate(student_data):
#     if i+1==index:
#         print(element)

#         marks=student_data.get(element)
#         avg=sum(marks)/len(marks)
#         print(avg)



# print name and avg in dictionary coprehansion
stdnt_avg_mrk={k:sum(v)/len(v) for k,v in student_data.items()}
print(stdnt_avg_mrk)


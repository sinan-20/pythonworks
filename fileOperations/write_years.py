# wrie 1800-2024

# write operation only support in string types


f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\years.txt","w")

for year in range(1800,2025):

    f.write(str(year)+"\n")

f.close()
years_path="C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\years.txt"

century_path="C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\century.txt"

leap_year_path="C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\leapyear.txt"


f_read=open(years_path,"r")

f_century=open(century_path,"w")

f_leap_year=open(leap_year_path,"w")

for year in f_read:

    year=int(year)

    if year%100==0:

        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leap_year.write(str(year)+"\n")

f_read.close()
f_century.close()
f_leap_year.close()


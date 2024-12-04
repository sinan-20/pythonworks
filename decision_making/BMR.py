

weight=int(input("enter your weight:"))
height=int(input("enter your height"))
age=int(input("enter age:"))
gender=input("enter gender").lower()
print(weight,height,age,gender)

if gender=="male":
    BMR=10*weight+6.25*height-5*age+5

elif gender=="female":
    BMR=10*weight+6.25*height-5*age-161

else:
    print("invalid gender")

print(BMR)

activity_level=int(input("""
select activity level
press 1 for sedantary
press 2 for lightly active
press 3 for modaratly active
press 4 for very active
press 5 for extra active
"""))

if activity_level==1:

    calorie=BMR*1.2

elif activity_level==2:

    calorie=BMR*1.375

elif activity_level==3:

    calorie=BMR*1.55

elif activity_level==4:

    calorie=BMR*1.725

elif activity_level==5:

    calorie=BMR*1.9



else:
    print("select valid choice for activity level")

print(f"total number of calories you need in order to maintain your current weight={calorie}")

target_weight=int(input("enter wight reduce in kg"))

durasion=int(input("enter duration in weeks"))

calorie_deficit=target_weight*7700

days=durasion*7

daily_calorie_deficit=calorie_deficit/days

print("daily_calorie_deficit",daily_calorie_deficit)




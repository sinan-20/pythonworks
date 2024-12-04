weight_in_kg=int(input("enter weight in kg:"))

height_in_cm=int(input("enter height in cm:"))

height_in_meter=height_in_cm/100

BMI=weight_in_kg/height_in_meter**2

BMI=round(BMI)

print(BMI)


if BMI<19:
    print("under weight")

elif BMI<25:
    print("normal weight")

elif BMI<30:
    print("over weight")

elif BMI>=30:
    print("obese")

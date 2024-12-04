

#BMI=weight_in_kg/(height_in_meter)**2

weight_in_kg=int(input("enter weight in kg:"))

height_in_cm=int(input("enter height in cm:"))

height_in_meter=height_in_cm/100

BMI=weight_in_kg/height_in_meter**2

BMI=round(BMI,2)

print(BMI)
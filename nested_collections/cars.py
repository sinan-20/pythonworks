cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

print(f"total number of vehicle=>{len(cars)}")

# # print available colors of baleno

available_color_of_baleno=[c.get("colors")for c in cars if c.get("name")=="baleno"]
print(available_color_of_baleno[0])

# # print all brands

all_brands={c.get("brand")for c in cars}
print("all_brands:",all_brands)
# #                   or
all_brands=[c.get("brand")for c in cars]
print(set(all_brands))


# # print car names in available in amt transmission

amt_transmission_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_transmission_cars)

# # car available in blue color

blue_color_cars=[c.get("name")for c in cars if "blue" in c.get("colors")]
print(blue_color_cars)

# # print all transmission types

all_transmission_types={t for c in cars for t in c.get("transmissions")}
print(all_transmission_types)

# # print all colors

all_color={col for c in cars for col in c.get("colors")}
print(all_color)

# most popular color

all_color=[col for c in cars for col in c.get("colors")]
# # print(all_color)
occurrences = {col: all_color.count(col) for col in all_color}
print("most popular color=>",max(occurrences))

# # costly car

cosltly_car=max(cars,key=lambda d:d.get("price"))
print(cosltly_car.get("name"))


# # car with minimum cost
low_cost=min(cars,key=lambda d:d.get("price"))
print(low_cost.get("name"))


# sort cars wrt price

sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)
sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_car}
print(sorted_car_name)


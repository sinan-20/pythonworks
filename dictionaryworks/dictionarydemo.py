
# create a dictionary product with keys id,title,price,brand

product={"id":101,"title":"vehicle","price":250000,"brand":"honda"}

print(product["price"])#disply product price


# update product price

product["price"]=450000

print(product)


# add use_by_date


product["use_by_date"]="25-09-2024"

print(product)

# update offer=5000

product["offer"]=5000

print(product)

# add offer as 10000 if offer exist else add offer as 20000

if "offer" in product:

    product["offer"]=10000

else:

    product["offer"]=20000

print(product)


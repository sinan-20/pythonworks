from json import load

f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\countreas.json",encoding="UTF-8")

data=load(f)

# print(len(data))

# print all contries name

all_contries=[country.get("name")for country in data]
# print(all_contries)

# print all region

all_region=[country.get("region")for country in data]
# print(set(all_region))

region_count={region:all_region.count(region)for region in all_region}
# print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count,region_count.get(max_region_count))

# usr_inpt=input("enter country")

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]
# print(country_capital)



# countries with most  number of borders

country_borders={country.get("name"):len(country.get("borders",[]))for country in data}
# print(country_borders)

max_border_country=max(data,key=lambda cntry:len(cntry.get("borders",[]))).get("name")
# print(max_border_country)

max_populated_cntry=max(data,key=lambda cntry:cntry.get("population",0)).get("name")
# print("most populated country:",max_populated_cntry)

# names of countries shared border

alpha_3_code=[cntry.get("borders") for cntry in data if cntry.get("name")=="India"][0]

for code in alpha_3_code:

    for cntry in data:

        if cntry.get("alpha3Code")==code:

            print(cntry.get("name"))
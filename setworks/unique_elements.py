
arr=[100,10,20,30,40,10,20,30,40]

# create empty set

st=set()

# fetch numbers from array

for num in arr:

    # add num to set

    st.add(num)

# display set

print(st)



# ---------------------------------------------

# intersection method------------------------

st1={10,20,30,40}

st2={10,20,50,60}

intersection_set=st1.intersection(st2)

print(intersection_set)

# union method ----------------------------

union_set=st1.union(st2)

print(union_set)

# diffrends method------------------------

diffrence_set=st1.difference(st2)

print("defrence",diffrence_set)

# remove method--------------------------

st1={10,20,30,40,50}

st1.remove(40)

print(st1)








# methods-----------------------------------------------



# add()

# intersection()

# union()

# remove()

# defference()

# issubset()

#  issuperset()

#  symmetric_diffrence() # (AUB)-(A^B)

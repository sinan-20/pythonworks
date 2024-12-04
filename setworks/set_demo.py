
st=set() #set

st={10,20,30,10,20,30,"hello","hai",True}

print(st)


# --------------------------------------

colors={"red","yellow","green"}

colors.add("blue")

print(colors)

# --------------------------------

colors=["red","yellow","green","red"]


colors_set=set(colors)


print("cll",colors_set)


# issubset----------------------------

st1={1,2,3}

st2={1,2,3,4,5,6,7}

print(st1.issubset(st2))


# issuperset ---------------------------------------

st1={1,2,3}

st2={1,2,3,4,5,6,7}

print(st2.issuperset(st1))

# symmetric_diffrence-------------------------------


st1={1,2,3,8,9}

st2={1,2,3,4,5,6,7}

symmetric_defrence=st1.symmetric_difference(st2)

print("symmetric diffrence",symmetric_defrence)


# update-------------------------


st1={1,2,3}

st2={1,2,3,4,5,6,7}


st1.update(st2)

print(st1)



text="this is a test to remove duplicate words this test is simple"

words=text.split(" ")

text2="this is simple test remove duplicate words"

# split text wrt space

words2=text2.split(" ")

is_subset=set(words2).issubset(set(words))



print(is_subset)

# print(set(words))







# set methods ----------------------------------------------------

# add()

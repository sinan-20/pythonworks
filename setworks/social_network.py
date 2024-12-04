

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

# follow_sugestion["sanju","pandya","siraj"]

rahul_follo_suggestion=set(users).difference(set(rahul_followers))

print("rahul follow sugestion",rahul_follo_suggestion)


mutual_frnds=set(rahul_followers).intersection(set(sanju_followers))

print("mutual friends ",mutual_frnds)
# -------------------------------------------------------------
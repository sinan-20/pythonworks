# is a kangaroo word???

source_word="REGULATE"
target_word="LATE"

# charcter_count={}

# for ch in source_word:

#     if ch in charcter_count:

#         charcter_count[ch]=+1

#     else:

#         charcter_count[ch]=1

# print(charcter_count)




character_count={ch:source_word.count(ch) for ch in source_word}

is_kangaroo_word=True

for ch in target_word:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

    else:

        is_kangaroo_word=False

print(is_kangaroo_word)






text="ABBACB"

word_count={}

for ch in text:

    if ch in word_count:

        word_count[ch]+=1

    else:

        word_count[ch]=1

print(word_count)


# another method----------------------------

text="ABBACBDFEDR"

charcter_frequency={ch:text.count(ch) for ch in text}



print(charcter_frequency)

# print non reccursieve elements

for k,v in charcter_frequency.items():

    if v==1:

        print(k)

# ----------------------------------------


non_recuursive_characters=[k for k,v in charcter_frequency.items() if v==1]

print(non_recuursive_characters)





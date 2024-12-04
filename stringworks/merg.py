

# text1="PQR"

# text2="ABC"

# result=""

# for i in range(0,len(text1)):

#     result+=text1[i]+text2[i]

# print(result)


            #another one

text1="PQRST"

text2="ABC"


smallest_text=text1 if len(text1)<len(text2) else text2

large_text=text1 if len(text1)>len(text2) else text2

result=""


for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

balnce_text=large_text[len(smallest_text):]

result+=balnce_text

print(result)


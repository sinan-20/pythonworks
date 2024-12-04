

text="pneumonoultramicroscopicsilicovolcanoconiosis"

text=text.capitalize()

v_count=0

c_count=0

vowel_sequence=("a","e","i","o","u")

for ch in text:

    if ch in vowel_sequence:

        v_count=v_count+1

    else:

        c_count=c_count+1

print("vowel count=",v_count)
print("consonent count=",c_count)


#print vowel count
#print consonants

for ch in text:

    if ch=="a" or ch=="e" or ch=="i" or  ch=="o" or ch=="u":

        print

    
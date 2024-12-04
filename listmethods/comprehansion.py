

arr=[3,5,2,9,6]

square=[num**2 for num in arr]#mapping(no codition)

print("squar list",square)


add_ten=[ num+10 for num in arr]#mapping
print("add ten",add_ten)


odd_numbers=[ num for  num in arr if num%2!=0]#filter
print("odd number",odd_numbers)

even_numbers=[num for num in arr if num%2==0]#filter
print("even number",even_numbers)

num_gt_five=[num for num in arr if num>5]#filter
print("num gt 5",num_gt_five)

text=["apple","orange","potatto","tomatto"]


starting_vowel=[w for w in text if w[0]  in ['a','e','i','o','u']]

# print(starting_vowel)

consonent_word=[w for w in text if w[0] not in ['a','e','i','o','u']]

print(consonent_word)


long=max([len(w) for w in text ])

longest_word=[ w for w in text if len(w)==long]

print(longest_word)

text=["apple","mundiri","orange","biriyani"]

starting_vowels=[w for w in text if w[0] not in ["a","e","i","o","u"]]
print(starting_vowels)


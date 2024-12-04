
text=" this is a simple programming question for find word with maximum number of charecters"

# step1 split text to words

# words=text.split(" ")

# def get_length(w):

#     return len(w)
# print(max(words,key=get_length))



# sorting this text 

# text=" this is a simple programming question for find word with maximum number of charecters"
# words=text.split(" ")
# def get_length(w):

#     return len(w)
# str_words=sorted(words,key=get_length,reverse=True)

# print(str_words)


# find frequent word 

text="this is a simple programming question for find word with maximum number of charecters"
words=text.split(" ")

def get_count(w):
    
    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)
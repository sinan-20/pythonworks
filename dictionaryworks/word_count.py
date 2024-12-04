

word=["hai","hello","hai","hello","hai","is"]

word_count={}


for w in word:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)



# return reccursieve words

word=["hai","hello","hai","hello","hai","is"]


word_frequency={w:word.count(w) for w in word }

# print(word_frequency)

reccursieve_word=[ k for k,v in word_frequency.items() if v>1]

print(reccursieve_word)


# word_count={w:word.count(w) for w in word}

# print(word_count)
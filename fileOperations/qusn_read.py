
f=open("C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\qusn.txt","r")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

word_count={w:words.count(w)for w in words}

nested_word_count=[[v,k]for k,v in word_count.items()]

print(sorted(nested_word_count,reverse=True))
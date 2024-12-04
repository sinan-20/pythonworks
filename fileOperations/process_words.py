
words_path="C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\words.txt"

pallindrom_path="C:\\Users\\ACER\\Desktop\\pythonworks\\datasets\\pallindrom.txt"


f_read=open(words_path,"r")

f_write=open(pallindrom_path,"w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_words=word[::-1]

    if word==reversed_words:

        f_write.write(word+"\n")

f_read.close()

f_write.close()


    



# text="hellopython"

# text=text.casefold()

# for ch in text:

#     if ch=="a" or ch=="e" or ch=="i" or  ch=="o" or ch=="u":

#         print(ch)
    

# text="hello world python"

# words=text.split(" ")

# print(words)



# text="\t this is \t  a line \t"

# new_text=text.strip("\t")

# print(new_text)


#strip()(both side remove)
#lstrip()(left side remove)
#rstrip()(right side remove)


# text="hello world program"

# new_text=text.replace("o","a")

# print(new_text)


#replace("old charcter", "new charcter")


# text="python programming"

# print(text[:6])


# print(text[7:])

# print(text[:7:2])

# string="hello"

# reverse_text=string[::-1]

# print(reverse_text)



# text=input("enter text:")

# reversed_string=text[::-1]

# print("pallindrom"if reversed_string==text else "not pallidrom")


# text=input("enter text:")

# length=len(text)-1

# reversed_string=""

# for i in range(length,-1,-1):

#     reversed_string=reversed_string+text[i]

# print("pallidrom" if reversed_string==text else "not pallindom")


# text="helloworld"

# print(text.index('o'))




text="sinanzinan@gmail.com"

# at_index=text.index("@")

# username=(text[:at_index])

# print(username)

        #or

# print(text[0:text.index("@")])




text="hellopython"

o_index=text.index("o")

reversed_sub_string=text[o_index-1::-1]

balnced_sub_string=text[o_index:]

result=reversed_sub_string+balnced_sub_string

print(result)






# string_object[start:end:step]


# print(text.capitalize())

# print(text.casefold())

# print(text.isalpha())

# print(text.isdigit())

# print(text.isalnum())

#print(text.startswith(str))






#capitalize()
#casefold()
#isalpha()
#isdigit()
#isalnum()
#startswith(str)
#endswith(str)


text="ABAABBC"

# most reccursieve charecter

# non reccursieve character
def get_count(char):
    return text.count(char)

most_reccursieve_charecter=max(text,key=get_count)

print(most_reccursieve_charecter)

least_reccursieve_charecter=min(text,key=get_count)

print(least_reccursieve_charecter)


    

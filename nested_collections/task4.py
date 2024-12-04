# sample_input="{}"

# op=>valid

user_input=input("enter bracket pairs:")

symbol_pairs={"{":"}","[":"]","(":")","<":">"}

symble_stack=[]

top=-1

is_valid=True

for symbol in user_input:

    if symbol in symbol_pairs:#symbol is an opening

        top=top+1
        
        symble_stack.append(symbol)#push the symbol to stack

    elif top==-1:#start in closing brackets

        is_valid=False
    
    elif symbol == symbol_pairs.get(symble_stack[top]):#chk symbol is a valid closing

        top=top-1

        symble_stack.pop()

    else:

        is_valid=False

if len(symble_stack)==0 and is_valid==True:

    print("valid")

else:

    print("invalid")







        









    



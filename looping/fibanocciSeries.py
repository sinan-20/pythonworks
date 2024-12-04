


prev=0

current=1

print(prev)

print(current)

for i in range(1,14):

    next=prev + current

    print(next)

    prev=current

    current=next


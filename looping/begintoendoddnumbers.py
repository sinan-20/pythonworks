

begin=int(input("enter begin:"))

end=int(input("enter the end:"))

if begin>end:

    begin,end=end,begin

i=begin

while(i<=end):

    if i%2!=0:

        print(i)

    i=i+1
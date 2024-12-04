# print list of expnses

expenses=[11000,10000,17000,15000,16000]

# for exp in expenses:

#     print(exp)

# ______________________________________________

   #          print total expence

# total=0

# for exp in expenses:

#     total+=exp

# print(total)

#__________________________________________________

# print max_expnce without using max()
# max_exp=0


# for exp in expenses:
#     if exp>max_exp:
#         max_exp=exp
# print(max_exp)




# ______________________________________

total=0

for tot in expenses:#11000

    total+=tot#0+11000+12000+......=71000

min_exp=total#71000

for exp in expenses:
      
      if exp<min_exp:

        min_exp=exp

print(min_exp)
    


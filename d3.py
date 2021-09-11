# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.
# (number of bugs)


# Def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)
##################################################################################################
#errors
#python is case sensitive.therefore def and Def , avg and Avg is different.
# print contains undefined variable
# we have defined variable named "avg" and in print function we have printed a variable 
# which isn't declared
# also in avg bracket is missing around number1+number2+number3
#with bracket:(1+2+3)/3=6/3=2
#without bracket:1+2+3/3=1+2+1=4 which isnt the average of three numbers
#also instead of normal division it is advisable to perform floor division
#################################################################################################
#correct code
def Avg(number1,number2,number3):
    avg=(number1+number2+number3)//3
    print(avg)
Avg(1,3,2)


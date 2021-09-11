# Niche diye gye code snippet ki output kya hoga?

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :#ex:20
#         modulus = number%10#2.0
#         sum+=modulus#0#2.0
#         number/=10#2
#     return sum

# print(sumofdigits(20))
# in the above code instead of normal division we should appply floor division
# therefore correct code is:
def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :#ex:20
        modulus = number%10#2.0
        sum = sum + modulus#0#2.0
        number = number // 10#2
    print(sum)
    return sum
sumofdigits(123)#this will only work if you use print function in defining the function itself
               #if you only use return ,you have to store the function in a variable and then print.i.e.
               #x=sumofdigits(17)
               #print(x)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<output>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# 6
# def primeorNot(num):     
#     if num > 1:#it will only take numbers more then 1,not even 1
#         for i in range(2,num):#all the numbers from 2 to the given number.i.e in this case 406
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break#break can be ysed only within a loop
#             else:#else block is at wrong place
#                 print(num,"is a prime number")

#     else:#for 1 or less than 1
#            print(num,"is not a prime number")
# primeorNot(407)
# this program will give result based on the respective i
# for example:
# consider number 9
# we are starting the loop from num 2
# therefore as 9 is not divisible by two, it will print 9 is a prime number,which is False
# next i value is 3
# 9 is divisible by 3
# therefore now it will print 9 is not a prime number and we have applied break statement under this block
# therefore now the loop will stop 
# this ain't the correct code
def primeorNot(num):     
    if num > 1:#it will only take numbers more then 1,not even 1 406
        for i in range (2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")
    else:#for 1 or less than 1
        print(num,"is neither a prime number nor a composite number")
primeorNot(407)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<output>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# 407 is not a prime number
# 11 times 37 is 407
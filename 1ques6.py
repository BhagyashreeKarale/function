# Yeh question 3 parts mein. Teenon parts ka code likh ke ek hi file mein submit karo.

# Question (Part 1)
# calculator naam ka ek function banao jo teen argument leta ho - number_x, number_y, operation. 
# number_x aur number_y mein hum humesha do integers denge 
# aur operation mein kaunsa operation karna hai woh denge. 

# Jaise: 
# Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.
# Agar operation mein "subtract" diya toh number_x aur number_y ko subtract kar ke return karenge.
# Agar operation mein "multiply" diya toh number_x ko number_y se multiply kar ke returna karega.
# Agar operation mein "divide" diya toh number_x ko number_y se divide kar ke return karega

# Neeche kuch function calls ke examples diye hue hain: 
# calculator(20, 25, "add") call karne pe 45 returna karega. 45 hume 20+25 karne se milega.
# calculator(40, 3, "subtract") call karne pe 37 return karega. 37 hume 40-3 karne se milega.
# calculator(10, 4, "multiply") call karne pe 40 return karega. 40 hume 10*4 karne se milega.
# calculator(40, 4, "divide") call karnse pe 10 return karega. 10 hume 40/3 karne se milega.
# def calculator(num1,num2,operator):
#     if operator == "add":
#         result = num1 + num2
#     elif operator == "substract":
#         result = num1 - num2
#     elif operator == "multiply":
#         result = num1 * num2
#     elif operator == "divide":
#         result = num1 / num2
#     return result
# sum=calculator(40, 3, "substract")
# print(sum)

# Function likhne ke baad, yeh kaam karne ke liye function call karo aur variable mein value daalo. 
# 24 aur 20 ko add karo aur number_1 variable mein value daalo
# 50 aur 60 ko multiply karo aur number_2 variable mein value daalo
# 80 aur 120 ko divide karo aur number_3 variable mein value daalo
# 90 aur 23 ko subtract karo aur number_4 variable mein value daalo
def calculator(num1,num2,operator):
    if operator == "add":
        result = num1 + num2
    elif operator == "substract":
        result = num1 - num2
    elif operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 / num2
    return result
# number_1=calculator(24, 20, "add")
# print(number_1)
# number_4=calculator(90, 23, "substract")
# print(number_4)
# number_2=calculator(50, 60, "multiply")
# print(number_2)
# number_3=calculator(120, 80, "divide")
# print(number_3)

# Question (Part 2)
# Ab input ka use kar ke user se 2 numbers input lo. 
# Note: Yeh karne ke liye koi function banane ki zaroorat nahi hai. 
# Fir calculator function ko 4 baar call kar ke inn dono numbers ko 
# add, subtract, multiply, divide karo aur result ko 4 alag variables mein daalo. 
# Woh variables ka naam yeh hoga: 
# add_result add operation ka result store karega
# subtract_result subtract operation ka result store karega
# multiply_result multiple operation ka result store karega
# divide_result divide operation ka result store karega
# Fir upar wale chaaron variables ko print karo. Final code ko submit karo :)
# ui1=int(input("Enter first number"))
# ui2=int(input("Enter second number"))
# addresult=calculator(ui1,ui2,"add")
# subtract_result=calculator(ui1,ui2,"substract")
# multiply_result=calculator(ui1,ui2,"multiply")
# divide_result=calculator(ui1,ui2,"divide")
# print(addresult)
# print(subtract_result)
# print(multiply_result)
# print(divide_result)
###########################################################################################
#using list
# operations=["add","substract","multiply","divide"]
# for i in operations:
#     print(calculator(ui1,ui2,i))
################################################################################################
# Question (Part 2)
# list_change naam ka ek function ka code likho jo 2 lists jisme integers arguments ki tarah le 
# aur fir unn lists ki woh items jo same index number (kram) pe hain unko multiply kar ke 
# ek nayi list return karvaye. 
# Aapko multiply karne ke liye calculator function ka use karna hai. 
# Normal tareeke se multiply nahi kar sakte ho. 
# Jaise agar hum function ko aise call karenge toh:
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
# Yahan multiple_list ki yeh value honi chaiye:
# [10, 200, 150, 100]
# 10, 5 aur 2 ko multiple kar ke aaya, 
# 200 10 aur 20 ko multiple kar ke, 
# 150 50 aur 3 ko, 
# 100 20 aur 5 ko.
def list_change(list1,list2):
    new_list=[]
    for i in range(len(list1)):
        new_list.append(calculator(list1[i],list2[i],"multiply"))
    return new_list
x=list_change([5, 10, 50, 20], [2, 20, 3, 5])
print(x)



# Question (Part 1)
# add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le 
# aur fir unka sum print karta hai. 
# Arguments ka naam number1 aur number2 hona chaiye. 
# def add_numbers(x,y):
#     print(x+y)
# # Input :-
# num1 = 56
# num2 = 12
# add_numbers(num1,num2)
# Output :- 68

# Question (Part 2)
# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho 
# aur fir same position wale integers ka sum print karta ho. 
# Same position waale 2 integers ka sum karne ke liye 
# Part 1 mein di gayi add_numbers waale function ka use karo. 
# Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print karega
def add_numbers_list(x,y):
    for i in range (len(x)):
        print(x[i]+y[i])
   

add_numbers_list([50, 60, 10],[10, 20, 13])#both lists length should be same
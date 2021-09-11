# Question 5
# Yeh question 2 parts mein hai. 
# Dono parts ka code same file mein likh ke submit karein.

# Question (Part 1)
# check_numbers naam ka ek function likhiye jo do numbers le 
# aur fir print kare "Dono even hain" agar dono numbers even (2 se divide hote hain) 
# nahi toh print kare "Dono numbers even nahi hai"
def check_numbers(x,y):
    if x % 2 ==0 and y % 2 !=0:
        print("only",x,"is an even number")
    elif y % 2 ==0 and x % 2 !=0:
        print("only",y,"is an even number")
    else:
        print(x,"and",y,"both aren't even numbers")
check_numbers(2,3)

# Question (Part 2)
# Ab ek check_numbers_list naam ka ek function likho 
# jo inetgers ki list ko arguments ki tarah le 
# aur fir check kare ki same index waale dono integers even hain ya nahi. 
# Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo.
def check_numbers_list(x,y):
    for i in range (len(x)):
        if int(x[i]) % 2 == 0 and int(y[i]) % 2 ==0:
            print(x[i],"and",y[i],"are even numbers")
        else:
            pass
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
# Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] 
# Toh usko yeh output deni chaiye:
# Ek function likhiye jo ki ek limit naam ka parameter lega 
# aur 0 se limit tak ke beech ke number jo ki 3 aur 5 ke multiples hain 
# unka sum print karega.jaisa ki niche dikhaya gya hai. 
# Input:- 3 aur 5 ke multiples => 3, 5, 6, 9, 10
def multiples(limit):
    sum=0
    for i in range(1,limit):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return(sum)
        
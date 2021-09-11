# Ek perfect() naam ka function define kijiye jo ki ek parameter lega 
# aur uss parameter ko hume check karana hai ki vo perfect number hain ya nahi. 
# Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers 
# ko print kare.
# [ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors 
# ( including 1 & excluding itself) ka sum uss number ke barabar hota hai. 
def perfect(num):
    sum=0
    for i in range (1,num):
        if num % i == 0:
            sum=sum+i
    if num % sum == 0:
        print(num,"is a perfect number")
#perfect numbers from 1-1000
for i in range (2,1001):
    perfect(i)
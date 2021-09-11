# Ek function define kijiye jo ki drivers ki speed check karega. 
# Aur ye function speed naam ka ek parameter lega. 
# Agar speed 70 se kam hai to ye “ok” print karega.
# Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 
# 1 point dega (ye 70 ko count nahi karega).
# example ke liye agar speed 80 hai to print karega “points:2” .
# Agar driver ko 12 points se jyaada points milte hai to , 
# function “License suspended” print karega.    
def speed_check(speed):
    if speed <= 70:
        return "OK"
    else:
        speed1 = (speed-70)//5
        if speed1 <= 12:
            return print("Point:",speed1)
        else:
            return print("License suspended")
speed_check(71)

# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega 
# aur 0 se limit tak ke beech ke sabhi even aur odd numbers ko 
# label ke saath print karega
def showNumbers(limit):
    for i in range (0,limit+1):
        if i % 2 == 0:
            print(i,"is even")
        else:
            print(i,"is odd")
showNumbers(1000)
# Ek function likho jo ki ek argument le jo number ho or 
# dictionary return karega jisme keys 1 se lekar argument ke number tak hogi 
# aur values unke squares honge.

def dic(limit):
    d=dict()
    for i in range(1,limit+1):
        (d[i])=(i*i)
    print(d)
dic(6)

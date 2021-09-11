# Ek function define karo jo ki input me 2 strings lega 
# aur dono strings me se jiski length jyaada hogi use print karega 
# aur agar dono strings ki length equal hui to dono ko line by line print karega . 
# Hint :- use len() builtin function..
def stringlen(string1,string2):
    if len(string1) > len(string2):
        print(string1)
    elif len(string1) < len(string2):
        print(string2)
    else:
        print(string1,"and",string2,"have equal lengths")
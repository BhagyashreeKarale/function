# Question 5
# Niche diye gye code snippet ki output kya hogi?

def  meal(day,time):
    if day=="sunday":#python will run this block only when the day is sunday
        if time=="breakfast":# is the time is breakfast it will retuen dosa and exit the function.
            return "dosa"# same steps ahead too
        elif time=="lunch":
            return "dal rice"
        elif time=="dinner":
            return "paneer and  chapati"
        else :
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "fried rice"
        elif time=="lunch":
            return "aloo rice"
        elif time=="dinner":
            return "chhole bhature"
        else :
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "aloo"
        elif time=="lunch":
            return "rajma rice"
        elif time=="dinner"    :
            return "veg-chapati"
        else :
            return "time not found"
            
print(meal("sunday","lunch"))
print(meal("monday","dinner"))
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<output>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# dal rice
# chhole bhature
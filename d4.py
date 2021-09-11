# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs)

# def voter(age):
# if age < 18:
#     print("eligible")
# else:
#     print("not eligible")
#     voter(20)
###############################################################################################
#errors
#indentation is missing
# function is called inside the function
######################################################################################################
#correct code:
def voter(age):
    if age < 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)
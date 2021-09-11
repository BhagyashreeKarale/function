# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.
# (number of bugs)

# function multi(a,b):
#     multiply=a*b
#     return multiply
# print(multi(3,4))
###########################################################################################
#errors
#keyword used to define function is incorrect.def keyword isn't used.
# so function isn't defined in the first place
############################################################################################
#correct code
def  multi(a,b):
    multiply=a*b
    return multiply
print(multi(3,4))
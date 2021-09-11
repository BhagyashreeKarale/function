# Neeche diye huye codes mai kuch bugs hai. Ab aapko error find kar ke unhe solve karne hai.(number of bugs)
# def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print(median)
#         else:
#             Print(far)
#     distance(20,30)
###############################################################################################
#errors:
# in elif and else block inside print parantheses quotation is missing
# in else block p of print is capitalized therefore python doesnt interpret that as a print function ehich it should
# to use the functio we need to use it outside the block where it is defined
#the place of distance(20,30) is incorrect
def distance(kms):
        if kms < 20:
            print("close")
        elif kms < 50:
            print("median")
        else:
            print("far")
distance(20,30)

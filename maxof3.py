# Write a Python function to find the Max of three numbers.
def maxof3(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is the largest among the given three values")
    elif num2>num1 and num2 >num3:
        print(num2,"is the largest among the given three values")
    else:
        print(num3,"is the largest among the entered values")





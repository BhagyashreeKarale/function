# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
def factorial(num):
    product=1
    for i in range (1,num+1):
        product=product*i
    print(product,"is the factorial of",num)
    return product
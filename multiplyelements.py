# Write a Python function to multiply all the numbers in a list. 
def listproduct(list):
    product=1
    for i in list:
        product=product*i
    print(product,"is the product of all the elements present in the list")
    return product
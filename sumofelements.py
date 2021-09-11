# Write a Python function to sum all the numbers in a list.
def listsum(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum,"is the sum of all the elements present in the list")
    return sum
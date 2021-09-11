# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(list):
    ulist=[]
    for i in list:
        if i not in ulist:
            ulist.append(i)
    print("Here is your unique list:\n",ulist)
    return ulist
# Write a Python function that checks whether a passed string is palindrome or not.
def palindromecheck(string):
    rlist=(string[::-1])
    if rlist == string:
        print("It is a palidrome")
    else:
        print("It isn't a palidrome")
# another one for palidrome:
def palidromecheck2(string):
    left_pos = 0
    right_pos = len(string) - 1
    while right_pos <= left_pos:
        if string[right_pos] != string[left_pos]:
            print("It isn't a palidrome")
            return False
        left_pos = left_pos + 1
        right_pos = right_pos - 1
        print("It is a palidrome")
        return True
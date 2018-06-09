


def is_palindrome(n):
    rev = 0
    temp = n
    while(n>0):
        rem = n%10
        rev = (rev*10)+rem
        n = n/10
    return rev==temp

n=int(input("enter a no:"))
#print("the reverse no:",rev)

if(is_palindrome(n)):
    print("the no is palindrime")
else:
    print("the no is not palindrome")
    

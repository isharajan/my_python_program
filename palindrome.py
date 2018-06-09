


def palindrome(n):
    rev = 0
    while(n>0):
        rem = n%10
        rev = rev*10+rem
        n = n/10
    return n

n=int(input("enter a no:"))
a=palindrome(n)

#print("the reverse no:",rev)
if(a==n):
    print("the no is palindrime")
else:
    print("the no is not palindrome")
    

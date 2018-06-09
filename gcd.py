def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))
GCD=gcd(x,y)
print(" Greatest Common Divisor is:",GCD)

    
    

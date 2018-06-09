n=int(input("enter a no:"))
total=0
while(n>0):
    rem=n%10
    total=total+rem
    n=n/10
    
print("the sum is" ,total)

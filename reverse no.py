n=int(input("enter a no:"))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n/10

print("the reverse no:",rev)   


a=int(input("enter a value:"))                           
b=int(input("enter b value:"))
print("1.add,2.sub,3.multiply,4,division")
choice=int(input("enter your choice: 1,2,3,4"))                 
if(choice==1):
    c=a+b
    print("the addition is",c)
elif(choice==2):
    c=a-b
    print("the sub is",c)
elif(choice==3):
    c=a*b
    print("the multiply is",c)
else:
    c=a/b
    print("the division is",c)

def sqare():
    e=c*c
    print("sqare of no is",e) 

def expo(a,b):
    
    c=a**b
    print("expo no is",c)
square=sqare()
expo=expo(a,b)



    

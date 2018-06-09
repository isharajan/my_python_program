
def search(a,key):
    for i in a:
        if(i==key):
            return i
    return -1
a=[10,20,30,45,78,90]
key=int(input("enter ano:"))
l=len(a)
ans=search(a,key)    
if(ans>=0):
    print("the no is  found")
else:
    print("the no is not found")



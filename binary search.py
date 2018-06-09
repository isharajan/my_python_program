def get_array():
	l = []
	for i in range(input("Enter N:")):
		l.append(input())
	return l
	
def search(a,key):
    high=len(a)-1
    low=0
    while(high>=low):
        mid=(high+low)/2
        if(key==a[mid]):
            return mid
        elif(key<a[mid]):
             high=mid-1
        else:
            low=mid+1
    return -1
	

a= get_array() #[10,20,30,40,50,60,78,98]
l=len(a)
key=int(input("enter a no:"))
ans=search(a,key)
if(ans>0):
    print("the element is found")
else:
    print("the  element is not found")

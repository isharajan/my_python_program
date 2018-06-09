n=int(input("enter n no:"))
list1=[]
for i in range(n):
    n=int(input("enter the no:"))
    list1.append(n)
   
print(list1) 
max=list1[0]
for i in list1:
    if (i>list1[0]):
        max=i
print("The maximum no is",max)


n=int(input("enter n no:"))
list1=[]
for i in range(n):
    n=int(input("enter the no:"))
    list1.append(n)
   
print(list1) 
min=list1[0]
for i in list1:
    if (i<list1[0]):
        min=i
print("The minimum mo is",min)

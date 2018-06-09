n=int(input("enter n no:"))
list1=[]
for i in range(n):
    n=int(input("enter the no:"))
    list1.append(n)
   
print(list1)
sum=0
for a in list1:
   # print(a)
    sum=sum+a
print("sum is",sum)
avarage=sum/len(list1)
print("the avarage is",avarage)
      

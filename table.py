def table(n,a):
    for i in range(n,a*n+1,n):
            print(i)


def table2(n,a):
    l=[]
    for i in range(n,a*n+1,n):
            l.append(i)    
    return l


def table3(n,a):    
    return range(n,a*n+1,n)


n=int(input("enter a table no"))
a=int(input("enter the no of values"))
res=table(n,a)
ans=table3(n,a)
print ans

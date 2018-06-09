def h2(arr,l,m,r):
    
    #print arr[l:m],arr[m:r]
    if m - l==1 or r-m:
        print 

def helper(arr,l,r):
    print 'r-l',r-l,arr[l:r]
    
    if l<r and r-l!=0:
        #print arr[l:r]
        m = (l+r-1)/2
        #print arr,s,e,m
        helper(arr,l,m)
        helper(arr,m,r)
        h2(arr,l,m,r)
        
def power(n,m):
    arr = [11*i for i in range(m)]
    helper(arr,0,len(arr))

power(3,7)

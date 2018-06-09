def jump(l,s=1):
    return jump(l,s+1) + jump(l,s+2) if s<l else 1

l = 2
print jump(l)

def feb(N):
    if N==0 or N==1:
        return N
    else:
        result = feb(N-1)+feb(N-2)
        print 0

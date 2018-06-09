arr = [
       ['a','b','c','d','e'],
       ['f','g','h','i','j'],
       ['k','l','m','n','o'],
       ['p','q','r','s','t'],
       ['u','v','w','x','y'],
      ]

def get_location(c):
    row = None
    for i in range(len(arr)):
        if c in arr[i]:
            row = i
            for j in range(len(arr[i])):
                if c==arr[i][j]:
                    col = j
                    break
        if row!=None:
            break
    return (row,col)

def oprate(r,c):

    if c>0:
        s = 'move Right\n'*c
        for i in range(c):
            print arr[r]
        print s
    if c<0:
        
        s = 'move left\n'*-c
        print s
    if r>0:
        s = 'move Down\n'*r
        print s
    if r<0:
        s = 'move up\n'*-r
        print s

def nav(l1,l2):
    
    r1,c1 = get_location(l1)
    r2,c2 = get_location(l2)

    r = r2 - r1
    c = c2 - c1
    #oprate(r,c)
    
    if c>0:
        c = 'move Right\n'*c
    if c<0:
        c = 'move left\n'*-c
    if r>0:
        r = 'move Down\n'*r
    if r<0:
        r = 'move up\n'*-r
    print c
    print r
    

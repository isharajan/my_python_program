# your code goes here

def set_remining_array(arr,pick_location):
    l = len(arr)
    n_arr= arr[:]
    if pick_location==0:
        try:
            n_arr[1]=None
            n_arr[-1]=None
        except:
            pass
    elif pick_location==l-1:
        try:
            n_arr[0]=None
            n_arr[pick_location-1]=None
        except:
            pass
    else:
        n_arr[pick_location-1]=None
        n_arr[pick_location+1]=None
    n_arr[pick_location]=None
    #print n_arr
    return n_arr

def get_max_value_location(arr):
    mx = max(arr)
    if mx == None:
        return -1
    for i in range(len(arr)):
        if arr[i]==mx:
            return i

def get_value(arr,pick_location):
    l = len(arr)
    m_arr = arr[:]
    n_t = []
    while(pick_location != -1):
        n_t.append(arr[pick_location]) 
        m_arr = set_remining_array(m_arr,pick_location)
        pick_location = get_max_value_location(m_arr)
    s = sum(n_t)
    #print s,n_t
    return s

def max_value(arr):
    l = len(arr)/2
    value = []
    for i in range(l):
        value.append(get_value(arr,i))
    return max(value)

N = raw_input()
arr = map(int,raw_input().strip().split())
print max_value(arr)

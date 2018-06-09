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
    return n_arr

def get_max_value_location(arr):
    mx = max(arr)
    for i in range(len)

def get_value(arr,pick_location):
    pass
    

def max_value(arr):
    l = len(arr)
    value = []
    for i in range(l):
        value.append(get_value(arr,i))

N = raw_input()
arr = []
#for _ in range(int(N)):
#    arr.append(int(raw_input()))
print  arr
#max_value(arr)

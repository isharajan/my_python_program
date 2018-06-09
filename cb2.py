class List:

    def __init__(self, value=None, next_node=None, arr=None):
        self.value = value
        self.next = next_node
        if arr != None:
            self.create(arr)

    def create(self,arr):
        node = self
        node.value = arr[0]
        for n in arr[1:]:
            node.next = List(value = n)
            node = node.next
        return self

    def didplay(self):
        while self!=None:
            print self.value,
            self = self.next
        
class Sequence(List):

    Hash = None
     
    def __init__(self,arr=None): 
        self.sequence = List(arr = self._get_sequence(arr))

    def hist(self,arr):
        hash_table = {}
        for n in arr:
            hash_table[n] = hash_table.get(n,0)+1
        print hash_table
        return hash_table
    def _get_sequence(self,arr):
        count = 0
        diff = None
        sequence_list = []
        hash_list = []
        arr_length = len(arr)
        for i in range(arr_length-1):
                cdiff = arr[i+1]-arr[i]
                if diff == cdiff:
                    count += 1
                if (diff!=cdiff and count>=2) or (count>=2 and i+1==arr_length-1):
                    print count,i
                    hash_list.append(self.hist(arr[i-count:i+1]))
                    sequence_list.append(List(arr = arr[i-count:i+1]))
                    print arr[i-count:i+1]
                    count = 1
                    diff = cdiff 
                elif diff!=cdiff:
                    diff = cdiff                      
        Sequence.Hash = List(arr = hash_list)
        return sequence_list

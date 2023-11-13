class node :

    def __init__(self,data,next = None ):
        self.data = data
        self.nxtnd = next
    def __repr__(self):
        return f"data ={self.data}"
class ll:

    def __init__(self):
        self.head = None
        self.count = 0
    def add(self,data):
        node = node(data,self.head)
        self.head = node 
    def __repr__(self) -> str:
        itr = self.head
        while itr:
            if itr == self.head:
                return ["head",itr]
            else:
                return["-->",itr]


n1 = node(1)
n2 = node(2)
ll.add(n1)
ll.add(n2)
print()
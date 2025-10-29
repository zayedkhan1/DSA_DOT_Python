class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
class DLinkedList:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1
    
    def printVal(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next
    
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
        self.length+=1
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp.value
            
    
dblkdlist=DLinkedList(5)
dblkdlist.append(21)
dblkdlist.append(92)
print("pop values:", dblkdlist.pop())
dblkdlist.printVal()
print("\nDoubly linked list length:",dblkdlist.length)

        
    

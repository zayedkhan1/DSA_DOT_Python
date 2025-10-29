from xml.dom.minidom import Node

#print method
def printValue(self):
    temp=self.head
    while temp is not None:
        print(temp.value)
        temp=temp.next
        
#append method
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
    return True

#pop method
def pop(self):
    if self.length==0:
        return None
    temp=self.tail
    if self.tail==1:
        self.head=None
        self.tail=None
    else:
        self.tail=self.tail.prev
        self.tail=None
        temp.prev=None
    self.length-=1
    return temp.value


    
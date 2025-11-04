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
    return temp.value #returning temp.value fro seeing this value

#prepend method
def prepend(self,value):
    new_node=Node(value)
    if self.length==0:
        self.head=new_node
        self.tail=new_node
    else:
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    self.length+=1
    return True

#pop first method
def pop_first(self):
    if self.length==0:
        return None
    temp=self.head
    if self.length==1:
        self.head=None
        self.tail=None
    else:
        self.head=self.head.next
        self.head.prev=None
        temp.next=None
    self.length-=1
    return temp.value #returning temp.value for seeing this value

#get method
def get(self,index):
     if index<0 or index>=self.length:
         return None
     temp=self.head
     if index<self.length//2: #first half e pawar jonno
         for _ in range(index):
             temp=temp.next
     else:
         temp=self.tail
         for _ in range(self.length-1,index,-1):
             temp=temp.prev
     return temp.value
        
# set method
def set_value(self,index,value):
    temp=self.get(index)
    if temp is not None:
        temp.value=value
        return True
    return False

#insert method
def insert(self,index,value):
    if index<0 or index>self.length:
        return False
    if index==0:
        return self.prepend(value)
    if index==self.length:
        return self.append(value)
    new_node=Node(value)
    temp=self.get(index-1)
    new_node.next=temp.next
    temp.next=new_node
    self.length+=1
    return True
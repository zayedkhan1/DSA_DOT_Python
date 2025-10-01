class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
    def print_value(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

        
            
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp #can't access get value directly if we use set method ,we need to accessing value directly when calling
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
lkdlist=LinkedList(3)
lkdlist.append(4)
lkdlist.append(67)

lkdlist.set_value(1,6)

lkdlist.print_value()

#accessing value directly when calling (remember)
node =lkdlist.get(0)
if node:
    print(node.value)
            
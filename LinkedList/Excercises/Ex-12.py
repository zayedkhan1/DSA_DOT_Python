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
    
    def append(self,value):
        new_node=Node(value)
        
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        
    def printValue(self):
        temp=self.head
        while temp is not None: 
            print(temp.value ,end=" ")
            temp=temp.next
            
            
            
            
            
            
my_lkdlist=LinkedList(4)
my_lkdlist.append(7)
my_lkdlist.append(90)

my_lkdlist.printValue()

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
        self.length +=1
    
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length -=1
        if self.length==0:
            self.tail=None
        return temp.value

my_linked_list=LinkedList(1)
my_linked_list.append(4)
my_linked_list.append(9)

print(my_linked_list.pop_first())
print(my_linked_list.pop_first())


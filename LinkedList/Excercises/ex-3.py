class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__ (self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    
    def print_value(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append_value(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def pop_value(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length -=1
        
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value

linked_list_value=LinkedList(5)
linked_list_value.append_value(7)
linked_list_value.append_value(6)

print(linked_list_value.pop_value())#6
print(linked_list_value.pop_value())#7
print(linked_list_value.pop_value())#5
print(linked_list_value.pop_value())#none
print(linked_list_value.pop_value())#none


        
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
    
    #print method
    def print_my_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    #append method
    def append_on_list(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

#example usage
my_linked_list=LinkedList(3)
my_linked_list.append_on_list(5)
my_linked_list.append_on_list(5)
my_linked_list.print_my_list()
        
        
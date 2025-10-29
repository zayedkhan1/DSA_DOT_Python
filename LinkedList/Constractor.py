# Linked List Constructor

# creating a node class
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
# creating a linked list class
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
# example usage
my_linked_list=LinkedList(4)
# accessing the attributes
print("head:",my_linked_list.head.value)
print("tail:",my_linked_list.tail.value)
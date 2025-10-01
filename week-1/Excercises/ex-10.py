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
    
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        prev=temp.next
        before=None
        for _ in range(self.length):
            prev=temp.next
            temp.next=before
            before=temp
            temp=prev

print("before reverse :")
lkdlist=LinkedList(2)
lkdlist.append(3)
lkdlist.append(4)

lkdlist.print_value()

print("after reverse :")
lkdlist.reverse()

lkdlist.print_value()
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
    
    def append_value(self,value):
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
        return temp.value


lkd_list=LinkedList(5)
lkd_list.append_value(6)
lkd_list.append_value(18)
lkd_list.append_value(97)


print('get function value :', lkd_list.get(1) )

# lkd_list.print_value()

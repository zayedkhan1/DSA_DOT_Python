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
        return True
        
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1
        return True 
       
  
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def insert(self,index,value):
        if index<0 or index>=self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append_value(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
        


lkd_list=LinkedList(5)
lkd_list.append_value(6)
lkd_list.append_value(18)
lkd_list.append_value(97)

lkd_list.insert(2,88)
lkd_list.print_value()




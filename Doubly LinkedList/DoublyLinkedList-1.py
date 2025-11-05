from operator import index


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
class DLinkedList:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1
    
    def printVal(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next
    
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
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp.value
    
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
        return temp.value
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length//2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        # return temp.value # for running set value we just need ot return temp
        return temp
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp :
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        before=self.get(index-1)
        after=before.next
        before.next=new_node
        new_node.prev=before
        new_node.next=after
        before.next=new_node
        after.prev=new_node
 
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp.value
    
        
dblkdlist=DLinkedList(5)
dblkdlist.append(21)
dblkdlist.append(92)
print("pop values:", dblkdlist.pop())
dblkdlist.printVal()
print("\nDoubly linked list length:",dblkdlist.length)

dblkdlist.prepend(66)
dblkdlist.prepend(99)
dblkdlist.printVal()
print("\nDoubly linked list length:",dblkdlist.length)

# dblkdlist.pop_first()
print("popping first value:",dblkdlist.pop_first())
print("after popping first value the linked list is:")
dblkdlist.printVal()
print("\nDoubly linked list length:",dblkdlist.length)

# dblkdlist.get(2)
print("value at index 2 is:",dblkdlist.get(2))  
print("value at index 4 is:",dblkdlist.get(4))  

dblkdlist.set_value(2,88)

dblkdlist.insert(1,77)
print("after inserting 77 at index 1 the linked list is:")
# print("set value at index 1 is:",dblkdlist.set_value(1,88))
dblkdlist.printVal()

dblkdlist.remove(2)
print("\nafter removing value at index 2 the linked list is:")
dblkdlist.printVal()
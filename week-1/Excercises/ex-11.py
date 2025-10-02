###################### Beginner Level #####################

#Q: Create and Traverse: Implement a linked list and print all elements!
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
    
    def ptint_value(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next
        print(" ")
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def search(self,target):
        temp=self.head
        index=0
        while temp:
            if temp.value == target:
                return f"target {target} found at index {index}"
            temp = temp.next
            index += 1
        return "target not found"
    
    def prepend(self,value):
        new_node=Node(value)
       # if self.head is not None:# same 
        if self.length==0:  #  same 
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length -= 1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
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
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        pre=temp.next
        before=None
        for _ in range(self.length):
            pre=temp.next
            temp.next=before
            before=temp
            temp=pre
       
lkdList=LinkedList(5)

#Q:Insert at End: Insert a node at the end of the linked list.
lkdList.append(15)
lkdList.append(87)
lkdList.append(93)

# Q: Insert at Beginning: Insert a node at the start of the linked list.
lkdList.prepend(2)

# Q: Delete Last Node: Remove the last node from the linked list.
lkdList.pop()

# Q: Delete First Node: Remove the first node from the linked list.
lkdList.pop_first()



# Q:Reverse Print (without modifying list): Print elements in reverse order .
lkdList.reverse()

# Q:Length of Linked List: Write a function to count the number of nodes.
print("total nodes in this LinkedList : ",lkdList.length)

# Q: Search Element: Check if a given value exists in the linked list.
print(lkdList.search(66))

lkdList.ptint_value()

#Q: set and get method

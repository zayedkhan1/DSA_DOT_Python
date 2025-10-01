# creating a linked list using nested dictionaries
from xml.dom.minidom import Node


head={
    "value": 10,
    "next": {
        "value": 20,
        "next": {
            "value": 30,
            "next":{
                "value": 40,
                "next": None
            }
        }
    }
}
# traversing the linked list
print(head)
print(head['value']) # 10
print(head['next']['value']) # 20
print(head['next']['next']['value']) # 30
print(head['next']['next']['next']['value']) # 40


#printing method creating

def print_list(self):
    temp=self.head
    while temp is not None:
        print(temp.value)
        temp=temp.next
        
#appending method creating
def append(self,value):
    new_node=Node(value)
    if self.head is None:
        self.head=new_node
        self.tail=new_node  
    else:
        self.tail.next=new_node
        self.tail=new_node
    self.length+=1
    return True #not necessary

#pop method creating
#if head and tail is none(empty)
def pop(self):
    if self.length==0:
        return None
#if head and tail is not empty
    temp=self.head
    pre=self.head
    while(temp.next):#while temp.next is not none
        pre=temp
        temp=temp.next
    self.tail=pre
    self.tail.next=None
    self.length -=1
    if self.length==0:
        self.head=None
        self.tail=None
    return temp.value #.value is for value(Testing purpose)
        

#prepend method
def prepend(self,value):
    new_node=Node(value)
    if self.length==0:
        self.head=new_node
        self.tail=new_node
    else:
        new_node.next=self.head
        self.head=new_node
    self.length +=1
    return True #optional

#pop first element

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
    
#Get function

def get(self,index):
    if index<0 or index>=self.length:
        return None
    temp=self.head
    for _ in range(index):
        temp=temp.next
    return temp.value

#Set_value function
def set_value(sefl,index,value):
    temp=sefl.get(index)#using get methos inside set method
    if temp is not None:
        temp.value=value 
        return True
    return False

#insert fuction

def insert(self,index,value):
    if index<0 or index>=self.length:
        return False
    if index==0:
        return self.prepend(value)#need to set return true
    if index==self.length:
        return self.append(value) #need to set return true
    new_node=Node(value)
    temp=self.get(index-1)
    new_node.next=temp.next
    temp.next=new_node
    self.length+=1
    return True

#remove function

def remove(self,index):
    if index<0 or index>=self.length:
        return None
    if index==0:
        return self.pop_first()
    if index==self.length-1:
        return self.pop()
    prev=self.get(index-1)
    temp=prev.next
    prev.next=temp.next
    temp.next=None
    self.length-=1
    return temp.value

#Reverse function
def reverse(self):
    temp=self.head
    self.head=self.tail
    self.tail=temp
    after=temp.next
    before=None
    for _ in range(self.length):
        after=temp.next
        temp.next=before
        before=temp
        temp=after
        
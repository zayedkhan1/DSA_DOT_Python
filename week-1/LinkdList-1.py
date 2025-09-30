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
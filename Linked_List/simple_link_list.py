class Node(object):
    def __init__(self,value):
        self.data = value
        self.next = None

class link_list():
    def __init__(self,value):
        self.head = Node(value)
        self.head.len =0
        print(self.head.data, self.head.next)
    
    def insertatend(self,value):
        new_node = Node(value)
        print(f"new node value is {new_node.data} and next is {new_node.next}")
        node = self.head
        while node.next is not None:
            node = node.next
        if self.ishead(node):
            print(f"we have only 1 node in the Linked list as value node data is {node.data} and next is {node.next} ")
        node.next = new_node
        self.display()
    
    def display(self):
        node= self.head
        print(node.data)
        count=0
        if self.ishead(node):
            print("Value at Head Node is", node.data)
        while node.next is not None:
            print("Value at node is ",node.data)
            count+=1
            node = node.next
        print(f"Value at tail node is {node.data}")
        if not self.ishead(node):
            count+=1 #### Add the tail node
    
        self.head.len = count
    def ishead(self,node):
        if node == self.head:
            return True
        else:
            return False
    
    def len_ll(self):
        self.display()
        return self.head.len
        


    def insertatfirst(self,value):
        new_node = Node(value)
        temp_node= self.head
        new_node.next = temp_node
        self.head = new_node
        self.display()
ll = link_list(40)



ll.display()

ll.insertatfirst(25)

ll.display()

ll.insertatend(30)

print(ll.len_ll())
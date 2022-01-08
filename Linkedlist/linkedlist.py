#creation of linkedlist
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class LinkedList:
    def __init__(self):
        self.headval = None
        
    #Traversing a linkedlist
    def display(self):
        showval = self.headval
        while showval is not None:
            print(showval.dataval, end ="->")
            showval = showval.nextval
        if showval is None:
            print("None", end ="")
    #inserting at the beginning
    def Begining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    #inserting at the end of the linked list
    def Ending(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        presentval = self.headval
        while presentval.nextval:
            presentval = presentval.nextval
        presentval.nextval = NewNode    
    #inserting data between two nodes
    def InBetween(self,middle_node,newdata):
        if middle_node is None:
            print("The chosen node is absent")
            
        NewNode = Node(newdata)
        temp = middle_node.nextval
        middle_node.nextval = NewNode
        NewNode.nextval = temp
   #removing node
   
val = LinkedList()
val.headval=Node(1)
val1 = Node(2)
val2 = Node(3)
#linking the first node to second and second to third
val.headval.nextval=val1
val1.nextval=val2
#adding a new val at the beginning
#val.Begining(0)
#adding a new val at the end
#val.Ending(4)
#adding a val in between nodes
val.InBetween(val.headval.nextval,5)
val.display()


        
"""
Given the head of a linked list, remove the nth node from the end of the list 
and return its head.
"""
#Definition for singly-linked list.
class ListNode:
 def __init__(self, val=0, next=None):
     self.val = val
     self.next = next
     
def removeNthFromEnd(head, n):
        
    #creating a dummy variable to place at the beginning of the list
    dummy = ListNode(0, head)
    
    #creating the pointers to keep track of the elements
    left = dummy
    right = dummy.next
    
    #shifting the right pointer to start at node n
    while n > 0 and right:
        right = right.next
        n -= 1
        
    #checking if there is a node while moving each pointer by one
    while right:
        left = left.next
        right = right.next
        
    #deletes the nth node from the end
    left.next = left.next.next
    
    return dummy.next   
    
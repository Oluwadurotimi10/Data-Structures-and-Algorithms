# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:10:35 2021

@author: JADESOLA
"""

#creation of linkedlist
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
class Solution:    
    def addTwoLinkedLists(self, l1,l2,carry=0):
    
        summ = l1.val + l2.val + carry
        result = ListNode(summ % 10)
        carry = summ // 10
        
        if l1.next is not None or l2.next is not None:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            result.next = self.addTwoLinkedLists(l1.next, l2.next, carry)
        result.printList()
        return result
    
        
    def printList(self):
        value = self.val
        print(value.val, end="->")
        if value.next == None:
            print("None")
            return 
        else:
            self.printList(value.next)
            
            
ans = Solution()
ans.addTwoLinkedLists(l1,l2)

        
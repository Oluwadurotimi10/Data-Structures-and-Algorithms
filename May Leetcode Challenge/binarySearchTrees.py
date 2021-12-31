# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:00:30 2021

@author: JADESOLA
"""

#add two numbers stored in a lonked list in reverse order and give the output as
#linkedlist
class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#tuple will be used        
class binarySearchTree:
    def insert(self, data):
        if isinstance(data, tuple) and len(data) == 3:
            node =  TreeNode(data[1])
            node.left = self.insert(data[0])
            node.right = self.insert(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node
    
    def treeToTuple(self,node):
        if node.left.key is None:
            return (None, node.key,node.right.key)
        elif node.right.key is None:
            return (node.left.key, node.key,None)
        elif  node.left.key is None and node.right.key is None:
            return (None, node.key, None)
        else:
            return (self.treeToTuple(node.left.key),node.key,self.treeToTuple(node.right.key))
        
        
    
tree = binarySearchTree()
node = tree.insert(((1,3,None), 2, ((None, 3, 4), 5, (6,7,8))))
print(node.left.right.key)

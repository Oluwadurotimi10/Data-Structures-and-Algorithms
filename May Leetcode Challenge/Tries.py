# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:37:09 2021

@author: JADESOLA
"""

# Trie data structure (prefix)
#assume all values are lowercase letters
#trie node class
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isWordEnd = False
     
class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word):
        m = self.root
        for c in word:
            if c not in m.children:
                m.children[c] = TrieNode(c)
            m = m.children[c]
        m.isWordEnd = True
        
    def search(self, word):
        m = self.root
        for c in word:
            if c not in m.children:
                return False
            m = m.children[c]
        return m.isWordEnd
    
    def prefix_search(self, prefix):
        m = self.root
        for c in prefix:
            if c not in m.children[c]:
                return False
            m = m.children[c]
        return True
  
    
#driver function
def main():
    #input words
    words = ["the", "a", "there", "mum","any","their"]
    output = ["Not present in the trie",
              "Present in trie"]
    
    #trie object
    trie = Trie()
    
    
    for w in words:
        trie.insert(w)
        
    #searching for different key
    print("{} ------- {}".format("these", output[trie.starts_with("the")]))
    print("{} ------- {}".format("mum", output[trie.starts_with("mu")]))
    print("{} ------- {}".format("any", output[trie.starts_with("an")]))
    
    
if __name__ == '__main__':
    main()
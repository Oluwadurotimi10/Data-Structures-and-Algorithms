

def WordFilter(words, prefix, suffix):

    """
    Design a special dictionary which has some words and allows you to search 
    the words in it by a prefix and a suffix.
    
    Implement the WordFilter class:
    
    WordFilter(string[] words) Initializes the object with the words in the 
    dictionary.
    f(string prefix, string suffix) Returns the index of the word in the 
    dictionary which has the prefix prefix and the suffix suffix. If there is more
     than one valid index, return the largest of them. If there is no such word in
     the dictionary, return -1.
     """
     
     #using tries data structure
     class Trie:
             def __init__(self):
                 self.children = [None]*26
                 
                 #is EndOfWord True if node represents end of the word
                 self.isEndOfWord = False
             
     
     class Node:    
             def __init__(self):
                 self.root = self.getNode()
                 
            def getNode(self):
                return Trie()
            
            def _charToIndex(self, ch):
                return ord(ch) - ord("a)
            
            def insert(self, key):
                start = self.root
                length = len(key)
                for level in range(length)
    for i in range(len(words)):
        store_dict = dict()
        front = ""
        back = ""
        for j in range(len(words[i])):
            front += words[i][j]
            store_dict[front] = "front"
            last = (len(words[i])-1)-j
            back = words[i][last] + back
            if back in store_dict:
                store_dict[back] = "both"
            else:
                store_dict[back] = "back"
            print(store_dict)
        if prefix in store_dict and (store_dict[prefix] == "front" or store_dict[prefix] == "both"):
            if suffix in store_dict and (store_dict[suffix] == "back" or store_dict[suffix] == "both"):
                index = max(index, i)               
    return index
    

words = ["abcaccbcaa", "accabaccaa"]
ans = WordFilter(words, "a","aa")
print(ans)
[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa",
   "cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],
    ["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],
    ["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],
    ["ccbca","cbcababac"]]
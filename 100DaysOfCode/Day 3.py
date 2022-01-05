"""
Return the longest palindromic substring from the string given.
"""

def longest_palindromic_substring(s):
    #pointers to keep track of the left and right elements
    l = 0
    r = 0
    longest_sub = ""
    length_longest_sub = 0
    #looping through each element as the center of the substring
    for i in range(len(s)):
        #for odd numbered substring
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if length_longest_sub < r-l+1:
                longest_sub = s[l:r+1]
                #print(longest_sub)
                length_longest_sub = len(longest_sub)
            l -= 1
            r += 1
            #print(l, r)
        
        #for even numbered substring
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if length_longest_sub < r-l+1:
                longest_sub = s[l:r+1]
                #print(longest_sub)
                length_longest_sub = len(longest_sub)
            l -= 1
            r += 1
            #print(l, r)
    return longest_sub

#test cases
s = "cbabc" 
s = "cbbc"
s = "hannah"
s = "bad"  
s = "cbbd"
s = "babad"
#calling function
print(longest_palindromic_substring(s))   
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

def valid_parenthesis(s):
    #stack to keep track of the brackets
    stack = []
    #a dictionary to map the open to the close bracket
    map_bracket = {')' : '(', '}' : '{', ']' : '['}
    
    #looping through the string
    for i in range(len(s)):
        if s[i] == "[" or s[i] == "{" or s[i] == "(":
            stack.append(s[i]) 
            #print(stack)
        else:
            if stack:
                top = stack.pop()
                if top != map_bracket[s[i]]:
                    return False
            #for when a closing bracket is seen and the stack is empty
            else:
                return False
    if not stack:
        return True
    
s = '()))'
print(valid_parenthesis(s))
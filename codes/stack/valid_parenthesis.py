""""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    Leetcode: Valid Parenthesis (20)
"""


def isValid(self, s: str) -> bool:
    self.stack = []
    self.map = {"(": ")", "{": "}", "[": "]"}

    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            self.stack.append(s[i])
        else:
            if len(self.stack) == 0:
                return False
            peek = self.stack[-1]
            if s[i] == self.map[peek]:
                self.stack.pop()
            else:
                return False
    if self.stack:
        return False
    return True
# Leetcode 125

def isPalindrome(self, s):
    clean_str = ""
    for i in s:
        if i.isalpha():
            clean_str += i.lower()
        elif i.isnumeric():
            clean_str += i
    return clean_str == clean_str[::-1]

# Two pointer solution
def isPalindrome(self, s):
    left_ptr = 0
    right_ptr = len(s) - 1

    while left_ptr < right_ptr:

        while left_ptr < right_ptr and not self.isAlphanumeric(s[left_ptr]):
            left_ptr += 1

        while left_ptr < right_ptr and not self.isAlphanumeric(s[right_ptr]):
            right_ptr -= 1

        if s[left_ptr].lower() != s[right_ptr].lower():
            return False
        left_ptr += 1
        right_ptr -= 1

    return True

def isAlphanumeric(self, val):
    return ord("A") <= ord(val) <= ord("Z") or ord("a") <= ord(val) <= ord("z") or ord("0") <= ord(val) <= ord("9")

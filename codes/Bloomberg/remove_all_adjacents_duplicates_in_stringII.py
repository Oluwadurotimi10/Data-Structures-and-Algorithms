# Leetcode 1209

# TC - O(n)  SC - O(n)

def removeDuplicates(self, s: str, k: int) -> str:
    stack = []
    ans = ''

    for i, char in enumerate(s):
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])

        if stack[-1][1] == k:
            stack.pop()
    for vals in stack:
        ans += vals[0] * vals[1]
    return ans


# TC - O(n)  SC - O(n)
def removeDuplicates(self, s: str, k: int) -> str:
    stack = []
    ans = ''
    i = 0

    for i in range(len(s)):
        if not stack or stack[-1][0] != s[i]:
            stack.append([s[i], 1])
        else:
            stack[-1][1] += 1
        if stack[-1][1] == k:
            stack.pop()

    if not stack:
        return ans
    for i in range(len(stack)):
        ans += stack[i][0] * stack[i][1]
    return ans
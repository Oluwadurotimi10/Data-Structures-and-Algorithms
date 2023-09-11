# Leetcode 1047

def removeDuplicates(self, s: str) -> str:
    stack = []

    for i in range(len(s)):

        if not stack:
            stack.append(s[i])
        else:
            curr = stack[-1]
            if curr != s[i]:
                stack.append(s[i])
            else:
                stack.pop()

    return ''.join(stack)

# Leetcode 1209  (The medium one)

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

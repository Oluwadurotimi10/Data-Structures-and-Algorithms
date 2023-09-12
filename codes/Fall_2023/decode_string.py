# Leetcode 394

def decodeString(self, s: str) -> str:
    stack = []

    for idx, c in enumerate(s):
        if c == "]":
            k = ""
            curr_str = ""
            while stack[-1] is not "[":
                curr_str = stack.pop() + curr_str
            stack.pop()
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            curr_str *= int(k)
            stack.append(curr_str)
        else:
            stack.append(c)

    return ''.join(stack)


# with better complexity
def decodeString(self, s: str) -> str:
    idx, num, stack = 0, 0, [""]
    str_length = len(s)

    while idx < str_length:
        if s[idx].isdigit():
            num = num * 10 + int(s[idx])
        elif s[idx] == "[":
            stack.append(num)
            num = 0
            stack.append("")
        elif s[idx] == "]":
            top_str = stack.pop()
            curr_num = stack.pop()
            full_str = stack.pop()
            stack.append(full_str + top_str * curr_num)
        else:
            stack[-1] += s[idx]
        idx += 1
    return ''.join(stack)
# Leetcode 394

def decodeString(self, s: str) -> str:
    stack = []
    for i in range(len(s)):
        if s[i] is not ']':
            stack.append(s[i])
        else:
            char = ''
            mul = ''
            while stack[-1] != '[':
                top = stack.pop()
                char = top + char
            stack.pop()
            while stack and stack[-1].isdigit():
                top = stack.pop()
                mul = top + mul
            stack.append(char * int(mul))

    return ''.join(stack)

#TC : O(m)

    def decodeString(self, s: str) -> str:
        num, stack = 0, []
        chars = ""
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
                continue
            if char == "[":
                stack.append([chars, num])
                chars = ""
                num = 0
            elif char == "]":
                prev_chars, prev_num = stack.pop()
                chars = prev_chars + chars * prev_num
            else:
                chars += char
        return chars

    

def decodeString(self, s: str) -> str:
    ite, num, stack = 0, 0, [""]

    while ite < len(s):
        if s[ite].isdigit():
            num = num * 10 + int(s[ite])
        elif s[ite] == "[":
            stack.append(num)
            num = 0
            stack.append("")
        elif s[ite] == "]":
            top_str = stack.pop()
            curr_num = stack.pop()
            full_str = stack.pop()
            stack.append(full_str + top_str * curr_num)
        else:
            stack[-1] += s[ite]
        ite += 1
    return "".join(stack)
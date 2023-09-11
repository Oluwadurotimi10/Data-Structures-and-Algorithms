""""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

"""


def calculate(self, s: str) -> int:
    stack = []
    curr_num = ""
    operand = '+'
    answer = 0

    for i in range(len(s)):
        if s[i].isdigit():
            curr_num += s[i]

        if (not s[i].isdigit() and s[i] != ' ') or (i == len(s) - 1):
            if operand == '+':
                stack.append(int(curr_num))
            elif operand == '-':
                stack.append(-1 * int(curr_num))
            elif operand == '*':
                top = stack.pop()
                stack.append(int(top * int(curr_num)))

            elif operand == '/':
                top = stack.pop()
                stack.append(int(top / int(curr_num)))

            operand = s[i]
            curr_num = ''

    while stack:
        answer += stack.pop()
    return answer

# Time complexity: O(N), Space complexity: O(N)


def calculate(self, s: str) -> int:
    last_num = 0
    curr_num = ""
    operand = '+'
    answer = 0

    for i in range(len(s)):
        if s[i].isdigit():
            curr_num += s[i]

        if (not s[i].isdigit() and s[i] != ' ') or (i == len(s) - 1):
            if operand == '+':
                answer += last_num
                last_num = int(curr_num)
            elif operand == '-':
                answer += last_num
                last_num = -1 * int(curr_num)
            elif operand == '*':
                last_num = last_num * int(curr_num)

            elif operand == '/':
                last_num = int(last_num / int(curr_num))

            operand = s[i]
            curr_num = ''

    answer += last_num
    return answer

# Time complexity: O(N), Space complexity: O(1)

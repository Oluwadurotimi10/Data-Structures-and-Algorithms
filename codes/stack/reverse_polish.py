""""
Leetcode (Evaluate Reverse Polish Notation)
"""

import operator

def evalRPN(tokens) -> int:
    stack = []
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    for i in range(len(tokens)):

        if tokens[i].isdigit() or (tokens[i].startswith('-') and tokens[i][1:].isdigit()):
            stack.append(int(tokens[i]))
        else:
            top1 = stack.pop()
            top2 = stack.pop()
            if tokens[i] == '/':
                num = int(ops[tokens[i]](top2, top1))
            else:
                num = ops[tokens[i]](top2, top1)
            stack.append(num)

    return stack[0]

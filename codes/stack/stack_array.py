# implementing stack using array
max_length = 100


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def isFull(stack):
    return len(stack) >= max_length


def pop(stack):
    if isEmpty(stack):
        return "Empty stack"
    else:
        return stack.pop()


def push(stack, value):
    if isFull(stack):
        return "Stack has reached maximum capacity"
    else:
        stack.append(value)
        return value, "is added to stack"


def peek(stack):
    if isEmpty(stack):
        return "Empty stack"
    else:
        return stack[-1]

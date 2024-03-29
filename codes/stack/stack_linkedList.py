class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode

    def pop(self):
        if self.isEmpty():
            return "Empty stack"
        top = self.root
        self.root = self.root.next
        return top.data

    def peek(self):
        if self.isEmpty():
            return "Empty stack"
        return self.root.data



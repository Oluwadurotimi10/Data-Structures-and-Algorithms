""""
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
     Leetcode: Min Stack (155)
"""

class MinStack:

    def __init__(self):
        self.main = []
        self.temp = []

    def push(self, val: int) -> None:
        self.main.append(val)

        if len(self.temp) == 0:
            self.temp.append(val)
        else:
            if val <= self.temp[-1]:
                self.temp.append(val)

    def pop(self) -> None:
        top = self.main.pop()
        if top == self.temp[-1]:
            self.temp.remove(top)
        return top

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        if self.temp:
            return self.temp[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
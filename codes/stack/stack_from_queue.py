""""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the
functions of a normal stack (push, top, pop, and empty).

Leetcode: Implement stacks using queues  (225)
"""
from queue import Queue


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.q = None

        self.size = 0

    def push(self, x) -> None:
        self.q2.put(x)
        self.size += 1
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self) -> int:
        if self.q1.empty():
            return

        self.size -= 1
        return self.q1.get()

    def top(self) -> int:
        if self.q1.empty():
            return -1

        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.size == 0

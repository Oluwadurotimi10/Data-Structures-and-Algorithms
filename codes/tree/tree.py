# Binary Tree

from queue import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def findVal(self, val):
        if self.data > val:
            if self.left_node is None:
                return f'{val} is not found'
            return self.left_node.findVal(val)
        elif self.data < val:
            if self.right_node is None:
                return f'{val} is not found'
            return self.right_node.findVal(val)
        else:
            return f'{self.data} is found'

    def insert(self, val):
        if not self.data:
            self.data = val
        else:
            if self.data < val:
                if self.right_node is None:
                    self.right_node = TreeNode(val)
                else:
                    self.right_node.insert(val)
            else:
                if self.left_node is None:
                    self.left_node = TreeNode(val)
                else:
                    self.left_node.insert(val)

    def printTree(self):
        if self.left_node:
            self.left_node.printTree()
        print(self.data,'->', end='')
        if self.right_node:
            self.right_node.printTree()

    # DFS
    def preOrder(self):
        print(self.data, '->', end='')
        if self.left_node:
            self.left_node.preOrder()
        elif self.right_node:
            self.right_node.preOrder()

    def inOrder(self):
        if self.left_node:
            self.left_node.inOrder()
        print(self.data, '->', end='')
        if self.right_node:
            self.right_node.inOrder()

    def postOrder(self):
        if self.left_node:
            self.left_node.postOrder()
        elif self.right_node:
            self.right_node.postOrder()
        print(self.data, '->', end='')

    # BFS
    def BFS(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            curr_node = queue.get()
            print(curr_node.data, '->', end='')

            if curr_node.left_node:
                queue.put(curr_node.left_node)
            if curr_node.right_node:
                queue.put(curr_node.right_node)

    def findMin(self):
        if self.left_node:
            return self.left_node.findMin()
        else:
            return self.data

        """"
            OR
            smallest = self.data

        if self.left_node:
            if self.left_node.data < smallest:
                self.left_node.findMin()
        else:
            print(smallest)
        """

    def findMax(self):
        largest = self.data

        if self.right_node:
            if self.right_node.data > largest:
                self.right_node.findMax()
        else:
            print(largest)

    def sumOfElements(self):
        summ = self.data
        if self.left_node:
            summ += self.left_node.sumOfElements()
        if self.right_node:
            summ += self.right_node.sumOfElements()
        return summ

    def height(self):
        left = 1
        right = 1
        if not self.left_node:
            return 0
        else:
            left += self.left_node.height()
        if not self.right_node:
            return 0


if __name__ == '__main__':
    root = TreeNode(5)
    root.insert(2)
    root.insert(-5)
    root.insert(1)
    root.insert(3)
    root.insert(-1)
    #root.printTree()
    print(root.sumOfElements())
    #print(root.height())


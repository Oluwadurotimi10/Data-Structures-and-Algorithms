# Leetcode 1656

class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = {i: "" for i in range(1, n + 1)}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ans = []
        if self.ptr == idKey:
            while self.ptr <= self.n and self.stream[self.ptr] != "":
                ans.append(self.stream[self.ptr])
                self.ptr += 1
        return ans


# without definitely defining a fixed dictionary size  (most optimal)
# TC: O(n)
class OrderedStream:

    def __init__(self, n: int):
        self.stream = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        output = []
        if idKey == self.ptr:
            while self.ptr in self.stream:
                output.append(self.stream[self.ptr])
                del self.stream[self.ptr]
                self.ptr += 1
        return output


# using list
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                self.ptr += 1
        return self.stream[idKey:self.ptr]

def minimumMoves(arr1, arr2):
    moves, val1, val2 = 0, 0, 0
    digit1, digit2 = 0, 0

    for i in range(len(arr1)):
        val1 = arr1[i]
        val2 = arr2[i]
        while val1 > 0:
            digit1 = val1 % 10
            digit2 = val2 % 10
            moves += abs(digit1 - digit2)
            val1 = (val1 - digit1) // 10
            val2 = (val2 - digit2) // 10
    return moves

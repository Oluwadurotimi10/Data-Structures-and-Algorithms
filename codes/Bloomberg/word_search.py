# Leetcode 79
from collections import Counter

def exist(board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])
    word_length = len(word)

    count = Counter()
    for i in range(rows):
        for j in range(cols):
            count[board[i][j]] += 1

    if word_length > rows * cols:
        return False

    if Counter(word) > count:
        return False

    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    def dfs(r, c, s):

        if s == len(word):
            return True

        if (0 <= r < rows and 0 <= c < cols and board[r][c] == word[s]):
            board[r][c] = '#'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            dp = any(dfs(r + i, c + j, s + 1) for i, j in directions)
            board[r][c] = word[s]
            return dp

        return False

    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0):
                return True
    return False
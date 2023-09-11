# Leetcode 2133

def checkValid(self, matrix):
    for r in range(len(matrix)):
        cols = set()
        rows = set()
        for c in range(len(matrix)):
            if matrix[r][c] in rows or matrix[c][r] in cols:
                return False
            rows.add(matrix[r][c])
            cols.add(matrix[c][r])

    return True

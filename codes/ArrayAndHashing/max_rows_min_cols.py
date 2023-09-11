# Fin the number that is maximum in its row and minimum in its column
from collections import Counter

def max_min(arr):
    row_col = set()
    res = []

    for rows in range(len(arr)):
        max_val = 0
        for c in range(len(arr[0])):
            max_val = max(max_val, arr[rows][c])
        row_col.add(max_val)

    for cols in range(len(arr[0])):
        min_val = float('inf')
        for r in range(len(arr)):
            min_val = min(min_val, arr[r][cols])
        if min_val in row_col:
            res.append(min_val)

    return res[0]


if __name__ == '__main__':
    arr = [[2,56,10],
           [19,35,12],
           [6,7,8]]

    print(min("aaa", "aab"))
    print(max_min(arr))
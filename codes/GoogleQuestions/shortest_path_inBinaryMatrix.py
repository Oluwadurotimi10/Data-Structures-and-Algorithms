# Leetcode 1091

# TC: O(m * n) , SC: O(m * n)
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    if rows == cols == 1:
        return 1

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

    queue = collections.deque()
    queue.append((0, 0, 1))
    visited = set()
    visited.add((0, 0))

    while queue:

        row, col, path = queue.popleft()

        for i, j in directions:
            r = row + i
            c = col + j

            if 0 <= r < rows and 0 <= c < cols:

                if grid[r][c] == 0 and (r, c) not in visited:
                    if r == rows - 1 and c == cols - 1:
                        return path + 1

                    queue.append((r, c, path + 1))
                    visited.add((r, c))

    return -1
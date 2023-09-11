# Leetcode 200

# bfs approach
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0
    visited = set()

    def bfs(r, c):
        queue = collections.deque()
        queue.append((r, c))
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            for i, j in directions:
                r = row + i
                c = col + j

                if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                    queue.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    return islands

# dfs approach

def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        if r == rows or c == cols or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == '0':
            return
        visited.add((r, c))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i, j in directions:
            row, col = r + i, c + j
            dfs(row, col)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    return islands


# dfs approach without using set

def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(r, c):
        grid[r][c] = '0'
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i, j in directions:
            row, col = r + i, c + j
            if row in range(rows) and col in range(cols) and grid[row][col] == '1':
                dfs(row, col)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                islands += 1

    return islands

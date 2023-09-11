# Leetcode 695

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    else:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):

            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            else:

                visited.add((r, c))
                """  
                return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1)) 
                """
                islands = 1
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for i, j in directions:
                    row, col = r + i, c + j
                    islands += dfs(row, col)
                return islands

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area

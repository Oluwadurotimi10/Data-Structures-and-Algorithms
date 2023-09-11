# Leetcode 1293

def shortestPath(self, grid: List[List[int]], k: int) -> int:
    if len(grid) == len(grid[0]) == 1:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    queue = collections.deque()
    visited = set()

    queue.append((0, 0, k, 0))
    visited.add((0, 0, k))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        row, col, obs, dist = queue.popleft()

        for i, j in directions:
            r = row + i
            c = col + j

            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] == 1 and obs > 0 and (r, c, obs - 1) not in visited:
                    queue.append((r, c, obs - 1, dist + 1))
                    visited.add((r, c, obs - 1))

                if grid[r][c] == 0 and obs >= 0 and (r, c, obs) not in visited:
                    if r == rows - 1 and c == cols - 1:
                        return dist + 1
                    queue.append((r, c, obs, dist + 1))
                    visited.add((r, c, obs))

    return -1
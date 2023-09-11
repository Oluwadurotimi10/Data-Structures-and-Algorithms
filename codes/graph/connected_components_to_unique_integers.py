import numpy as np


def connected_components(arr):
    # number of rows and columns in the array
    rows, cols = len(arr), len(arr[0])
    new_val = 0
    new_val_list = [0]

    def dfs(r, c, new_val):
        """"
            recursive function to check for connected components
        """

        # the possible directions you can go from a cell, (left, right, up and down)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        # check if row and col is within bounds and if the cell contains 1
        if r >= 0 and r < rows and c >= 0 and c < cols and arr[r][c] == 1:
            arr[r][c] = new_val

            # recursive call to every possible directions
            for i, j in directions:
                row = r + i
                col = c + j

                dfs(row, col, new_val)

    # loops to go through every cell in the array
    for row in range(rows):
        for col in range(cols):
            if row >= 0 and row < rows and col >= 0 and col < cols and arr[row][col] == 1:
                # check if the integer number has been assigned to a connected component
                if new_val in new_val_list:
                    new_val = np.random.randint(2, 9)
                    new_val_list.append(new_val)
                # call to check for connected components
                dfs(row, col, new_val)

    return arr


if __name__ == '__main__':

    # example input
    arr = [[1, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0]]

    print(connected_components(arr))

    """
    example output
    [[7, 0, 5, 5, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [3, 3, 3, 0, 0, 0]]
    """
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:53:41 2021

@author: JADESOLA
"""

def SetMatrixZero(matrix):
    #setting the elements in first row to
    rows = len(matrix)
    columns = len(matrix[0])
    rowZero = False
    
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    rowZero = True
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    for i in range(rows):
        if matrix[0][0] == 0:
            matrix[i][0] = 0
    for j in range(columns):
        if rowZero:
            matrix[0][j] = 0
    return matrix   
arr = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
#arr = [[0,1,1],[1,0,1],[1,1,1]]
#arr[1:3] = 0
print(SetMatrixZero(arr))



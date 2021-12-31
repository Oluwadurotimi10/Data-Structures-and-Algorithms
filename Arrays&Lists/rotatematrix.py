# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:09:17 2020

@author: JADESOLA
"""

def rotateMatrix(arr):
    """
        This function takes in a 2D matrix and rotates the matrix by 90 degrees
    """
    #first step is to transpose the matrix
    temp = 0
    N = len(arr) 
    for i in range(N):
        for j in range(i,N):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
    
    """        
    #swapping the elements horizontally to complete clockwise rotation
    for i in range(N):
        for j in range(N//2):
            temp = arr[i][j]
            arr[i][j] = arr[i][N-1-j]
            arr[i][N-1-j] = temp
    """ 
    #second step       
    #swapping the elements vertically to complete anti-clockwise rotation
    for i in range(N//2):
        for j in range(N):
            temp = arr[i][j]
            arr[i][j] = arr[N-1-i][j]
            arr[N-1-i][j] = temp
    
    return arr
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateMatrix(arr))
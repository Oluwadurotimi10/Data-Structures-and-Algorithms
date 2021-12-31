# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:49:53 2020

@author: JADESOLA
"""

def bestScore(arr):
    """
        This function takes in an array of scores and returns the first and second best scores
    """
    firstBest = 0
    secondBest = 0
    for i in range(len(arr)):
        if arr[i] > firstBest:
            secondBest = firstBest
            firstBest = arr[i]
        elif (arr[i] > secondBest) and (arr[i] < firstBest):
            secondBest = arr[i]
    print("The first best score is {} and the second best is {}".format(firstBest,secondBest))

arr = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
bestScore(arr)
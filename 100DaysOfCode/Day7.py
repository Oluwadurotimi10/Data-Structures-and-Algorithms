"""
An hourglass is a subset of values with indices falling in this pattern in's 
graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass
sum. 
"""

def hourglassSum(arr):
    max_sum = -1000
    summ = 0
    # Write your code here
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            summ = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            max_sum = max(max_sum , summ)
    return max_sum

arr = [[-9, -9, -9, 1, 1, 1 ],
       [0, -9,  0,  4, 3, 2],
       [-9, -9, -9,  1, 2, 3],
       [0,  0,  8,  6, 6, 0],
       [0,  0,  0, -2, 0, 0],
       [0,  0,  1,  2, 4, 0]]
print(hourglassSum(arr)) 

 
 
 
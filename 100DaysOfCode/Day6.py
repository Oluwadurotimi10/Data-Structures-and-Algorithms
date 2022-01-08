"""
Given an array  of n integers and a number, , perform d left rotations on the array.
Return the updated array to be printed as a single line of space-separated integers.
"""

#Using extra space
def rotLeft(arr, d):
    """
    arr_rot = []
    d_copy = d
    for i in range(len(arr)):
        if d < len(arr):
            arr_rot.append(arr[d])
            d += 1
    for j in range(len(arr[:d_copy])):
        arr_rot.append(arr[j])
    return arr_rot
    """
    
    #OR better approach
    return arr[d:] + arr[:d]

arr = [1,2,3,4,5]
print(rotLeft(arr, 1))
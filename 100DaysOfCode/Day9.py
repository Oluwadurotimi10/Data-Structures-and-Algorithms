"""
"""
"""
#first thought
def minimum_swaps(arr):
    i = 0
    temp = 0
    swaps = 0 
    
    while i < len(arr):
        if arr[i] != i + 1:
           temp = arr[arr[i]-1]
           arr[arr[i]-1] = arr[i]
           arr[i] = temp
           swaps += 1
        elif arr[i] == i + 1:
            i += 1
            
    return swaps
#Time complexitiy O(n), space complexity O(1)
"""    
#optimized
def minimum_swaps(arr):
    
    temp_arr = arr.copy()
    arr_map = {}
    temp_arr.sort()
    temp = 0
    swaps = 0
    
    for i in range(len(arr)):
        #mapping the unsorted arr to its index
        arr_map[arr[i]] = i
   
    for j in range(len(arr)):
        if arr[j] != temp_arr[j]:
            temp = arr[j]
            arr[j], arr[arr_map[temp_arr[j]]] = arr[arr_map[temp_arr[j]]], arr[j]
            
            #updating their positions in the map
            arr_map[temp] = arr_map[arr[j]]
            arr_map[arr[j]] = j
            swaps += 1
            
    return swaps

#Time complexitiy O(log n) , space complexity O(n) 
    
arr = [7,1,3,2,4,5,6]
arr = [4,3,1,2]
print(minimum_swaps(arr))    
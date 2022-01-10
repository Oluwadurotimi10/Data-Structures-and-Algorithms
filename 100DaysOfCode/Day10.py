"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation
 add a value to each the array element between two given indices, inclusive. Once all
 operations have been performed, return the maximum value in the array.

Example


Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of k between the indices a and b inclusive:
    
"""

#using prefix sum approach.
def array_manipulation(n, queries):
    max_num = 0
    #creating a new array to store the arithemetic carried out
    arr = [0 for j in range(n+1)]
    summ = 0
    
    for i in range(len(queries)):
        #adding the third element in each query to the position given by the first element
        arr[queries[i][0]-1] += queries[i][2]
        #subtracting the third element from the position given by the second element
        arr[queries[i][1]] -= queries[i][2]
    
    for j in range(len(arr)):
        #obtaining the prefix sum after all the operations has been carried out
        summ += arr[j]
        max_num = max(max_num, summ)        
            
    return max_num
n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]
print(array_manipulation(n, queries))
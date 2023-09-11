def insertion_sort(arr):


    for i in range(1,len(arr)):
        val = arr[i]
        k = i
        for j in range(i-1, -1, -1):
            if arr[j] > val:
                arr[j+1] = arr[j]
                k = j
        arr[k] = val

    return arr

    """
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
    
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
        return arr
    
    """

arr = [9,8,7,0,4,2,9]


print(insertion_sort(arr))



def selection_sort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    return arr
arr = [7,8,0,4,2,6]
print(selection_sort(arr))


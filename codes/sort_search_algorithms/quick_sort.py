def quick_sort(arr, left, right):
    if left < right:
        partition_idx = partition(arr, left, right)
        quick_sort(arr, left, partition_idx-1)
        quick_sort(arr,partition_idx+1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    #method 1
    # i keeps track of the index smaller values
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

    """
    #method 2
    i = left 
    j = right - 1

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = pivot, arr[i]
    return i
    """
arr = [9,8,7,0,4,12,9]

print(quick_sort(arr, 0, len(arr)-1))

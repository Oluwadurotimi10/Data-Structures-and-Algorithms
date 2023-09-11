# using array and using 1 indexed

# TC : Olog(N)
def max_heap(arr, i, N):
    left_idx = 2 * i
    right_idx = 2 * i + 1

    if left_idx <= N and arr[left_idx] > arr[i]:
        largest = left_idx
    else:
        largest = i
    if right_idx <= N and arr[right_idx] > arr[i]:
        largest = right_idx

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        max_heap(arr, largest, N)


# building max heap (we're not running on the leaf nodes since they are a single node heap)
# TC : O(N/2)
def build_maxheap(arr):
    for i in range(N/2, 0, -1):
        max_heap(arr, i)

"""
    For min heap
"""
# TC : Olog(N)
def min_heap(arr, i, N):
    left_idx = 2 * i
    right_idx = 2 * i + 1

    if left_idx <= N and arr[left_idx] < arr[i]:
        smallest = left_idx
    else:
        smallest = i
    if right_idx <= N and arr[right_idx] < arr[i]:
        smallest = right_idx
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heap(arr, smallest, N)


# building min heap (we're not running on the leaf nodes since they are a single node heap)
# TC : O(N/2)
def build_minheap(arr):
    for i in range(N/2, 0, -1):
        min_heap(arr, i)


# heap sort
# TC: O(NlogN) -> max_heap runs for O(logN) times and max_heap is run N-1 times. i.e O(N) (4 build_minheap)
# + O(NlogN) (min_heap)

def heapsort(arr):
    N = len(arr)
    heap_size = N
    build_maxheap(arr)
    for i in range(N-1, 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heap_size = heap_size - 1
        max_heap(arr, 1, heap_size-1)

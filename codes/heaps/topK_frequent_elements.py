# Leetcode 347
# using only maps (bucket sort)
# TC : O(MN)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    map_count ={}
    output = []
    freq = [[] for i in range(len(nums) + 1)]

    for i in range(len(nums)):
        map_count[nums[i]] = map_count.get(nums[i], 0) + 1

    for i, j in map_count.items():
        freq[j].append(i)

    for p in range(len(freq)-1, -1, -1):
        for vals in freq[p]:
            output.append(vals)
            if len(output) == k:
                return output


# using heap
# TC: O(KlogD + DlogD) , D is the number of distinct items. Constructing priority queue with D elements takes O(DlogD)
# to remove top priority element from heap it takes O(logD) then for k elements it takes O(KlogD)
# SC: O(D) for the count_map
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count_map = collections.Counter(nums)
    output = []

    # using heap
    heap = [(value, key) for key, value in count_map.items()]

    # get the top k elements using priority queue
    largest = heapq.nlargest(k, heap)

    for i, j in largest:
        output.append(j)
    return output


# Leetcode 347

def topKFrequent(self, nums, k):
    hashmap = {}
    output = []
    freq = [[] for i in range(len(nums) + 1)]

    for j in range(len(nums)):
        hashmap[nums[j]] = hashmap.get(nums[j], 0) + 1

    for p, q in hashmap.items():
        freq[q].append(p)

    for vals in range(len(freq) - 1, 0, -1):
        for val in freq[vals]:
            output.append(val)
            if len(output) == k:
                return output
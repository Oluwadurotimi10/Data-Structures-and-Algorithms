# Leetcode 49

# optimized     TC -> O(m.n)
def groupAnagrams(self, strs):
    hashmap = defaultdict(list)

    for i in strs:
        count = [0] * 26
        for j in i:
            count[ord(j) - ord('a')] += 1
        hashmap[tuple(count)].append(i)
    return hashmap.values()

# less optimized  TC -> O(m.nlogn)
def groupAnagrams(self, strs):
        output = []
        hashmap = {}
        for i, s in enumerate(strs):
            val = list(s)
            val.sort()
            val = ''.join(map(str, val))
            if val not in hashmap:
                hashmap[val] = []
            hashmap[val].append(i)

        for j in hashmap.values():
            group = []
            for idx in j:
                group.append(strs[idx])
            output.append(group)

        return output

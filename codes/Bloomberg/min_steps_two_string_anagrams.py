# Leetcode 1347
from collections import Counter


# TC: O(n), SC: O(s+t)
def minSteps(self, s: str, t: str) -> int:
    map_s = Counter(s)
    map_t = Counter(t)

    min_steps = 0
    for char in map_s:
        diff = map_s[char] - map_t[char]
        if diff >= 0:
            min_steps += diff

    return min_steps

"""
        {l:1,e:3,t:1,c:1,o:1,d:1}, {p:1,r:1,a:1,c:2,t:1,i:1,e:1}
            ms = 5
        """

# or
def minSteps(s: str, t: str) -> int:

		common = Counter(s) & Counter(t)
		count = sum(common.values())

		return len(s) - count


# using one hashmap
def minSteps(self, s: str, t: str) -> int:
    map_s = Counter(s)

    min_steps = 0
    for char in t:
        if char in map_s and map_s[char] > 0:
            map_s[char] -= 1

    return sum(map_s.values())





#  Leetcode 2186
from collections import Counter

# TC: O(s+t), SC: O(s+t)
def minSteps(s: str, t: str) -> int:

    map_s = Counter(s)
    map_t = Counter(t)
    min_steps = 0
    for char in map_s:
        min_steps += abs(map_s[char] - map_t[char])

    for char in map_t:
        if char in map_s:
            continue
        min_steps += abs(map_t[char] - map_s[char])

    return min_steps


# or
import string

def minSteps( s: str, t: str) -> int:
    sCount, tCount = Counter(s), Counter(t)
    return sum(abs(sCount[character] - tCount[character]) for character in string.ascii_lowercase)

# e.g, if s = leetcode, t = coaest


if __name__ == '__main__':
    s = "cotxazilut"
    t = "nahrrmcchxwrieqqdwdpneitkxgnt"
    print(minSteps(s, t))


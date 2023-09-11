# Leetcode 3

def lengthOfLongestSubstring(self, s: str) -> int:
    long = 0
    seen = set()
    substring = ''

    for i in range(len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            while s[i] in substring:
                substring = substring[1:]

        substring += s[i]
        long = max(long, len(substring))

    return long

## OR
def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    seen = set()
    long = 0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[i])
        long = max(long, i - l + 1)

    return long

# Leetcode 424

def characterReplacement(self, s: str, k: int) -> int:
    hashset = {}
    l, r = 0, 0
    long = 0
    maxF = 0

    for r in range(len(s)):
        hashset[s[r]] = hashset.get(s[r], 0) + 1
        maxF = max(maxF, hashset[s[r]])

        if (r - l + 1) - maxF > k:
            hashset[s[l]] -= 1
            l += 1
        long = max(long, r - l + 1)

    return long
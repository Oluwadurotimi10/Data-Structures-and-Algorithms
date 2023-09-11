# Leetcode 1048

def longestStrChain(self, words: List[str]) -> int:
    dp = {}
    ans = 1

    words.sort(key=len)

    for word in words:
        dp[word] = 1
        for c in range(len(word)):
            prev = word[:c] + word[c + 1:]
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
                ans = max(ans, dp[word])

    return ans
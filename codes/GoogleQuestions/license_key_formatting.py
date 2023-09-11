# Leetcode 482

def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = s.replace('-', '').upper()
    length = len(s)
    result = ''
    start = length % k
    if length == 1:
        return s

    result += (s[0:start])

    for i in range(start, length, k):
        if len(result) > 0:
            result += '-'
        result += s[i:i + k]

    return result
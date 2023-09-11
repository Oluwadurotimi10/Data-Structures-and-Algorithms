# Leetcode 692
# using only maps
# TC : O(MN)
# SC: O(PlogN)  P for values with same frequency
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    count_map = collections.Counter(words)
    output = []
    freq = [[] for i in range(len(words) + 1)]

    for word, count in count_map.items():
        freq[count].append(word)

    for j in range(len(freq) - 1, -1, -1):
        freq[j].sort()
        for vals in freq[j]:
            output.append(vals)
            if len(output) == k:
                return output

def topKFrequent(self, words, k):
    counts = collections.Counter(words)
    items = list(counts.items())
    items.sort(key=lambda item: (-item[1], item[0]))
    return [item[0] for item in items[0:k]]


# using heap
import heapq
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    count_map = collections.Counter(words)
    output = []
    freq = [[] for i in range(len(words) + 1)]

    for word, count in count_map.items():
        freq[count].append(word)

    for vals in range(len(freq) - 1, -1, -1):
        smallest = heapq.nsmallest(k, freq[vals])
        if smallest:
            for j in smallest:
                if len(output) < k:
                    output.append(j)
                else:
                    return output
    if len(output) == k:
        return output
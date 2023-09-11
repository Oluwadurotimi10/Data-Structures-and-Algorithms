# Leetcode 253

# TC: O(nlogn)  SC:O(n)
import heapq
"""
def minMeetingRooms(intervals) -> int:
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    count, rooms = 0, 0
    s, e = 0, 0

    while s < len(start):

        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            e += 1
            count -= 1
        rooms = max(rooms, count)
    return rooms
"""
# using heaps


def minMeetingRooms(intervals):
    intervals.sort()
    print(intervals)
    heap = []

    for s, e in intervals:
        # a room has just been emptied, using heap[0] since it is a minheap
        if heap and s > heap[0]:
            heapq.heapreplace(heap, e)
        # a new room is desired
        else:
            heapq.heappush(heap, e)
        print(heap)

    return len(heap)

if __name__ == '__main__':
    intervals = [[0, 30], [5, 30], [31, 40]]
    print(minMeetingRooms(intervals))
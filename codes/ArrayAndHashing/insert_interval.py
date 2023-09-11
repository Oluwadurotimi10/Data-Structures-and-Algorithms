# Leetcode 57

# TC : O(nlogn), SC : O(n)
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    intervals.append(newInterval)
    intervals.sort()

    output = [intervals[0]]

    for start, end in intervals:
        prev_start, prev_end = output[-1]

        if prev_end >= start:
            new_end = max(prev_end, end)
            output[-1][1] = new_end
        else:
            output.append([start, end])
    return output

# TC : O(n), SC : O(n) or O(1)
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    output = []
    i = 0

    while i < len(intervals) and newInterval[0] > intervals[i][1]:
        output.append(intervals[i])
        i += 1

    while i < len(intervals) and newInterval[1] >= intervals[i][0]:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        print(newInterval)
        i += 1

    output.append(newInterval)
    output.extend(intervals[i:])
    return output

# Leetcode 56

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
        return intervals

    intervals.sort()
    output = [intervals[0]]

    for start, end in intervals[1:]:
        prev_start, prev_end = output[-1]
        if prev_end >= start:
            output.pop()
            output.append([min(prev_start, start), max(prev_end, end)])
        else:
            output.append([start, end])
    return output


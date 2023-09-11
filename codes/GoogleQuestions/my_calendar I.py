# Leetcode 729

# TC: O(log N) & O(N) for insertion -> O(N log N)    SC: O(N)
class MyCalendar:

    def __init__(self):
        self.calendar = [[-1, -1],[float('inf'),float('inf')]]

    def book(self, start: int, end: int) -> bool:
        l = 0
        r = len(self.calendar)

        while l < r:
            mid = l + (r-l)//2

            if end == self.calendar[mid][0]:
                l = mid
                break
            else:
                if end > self.calendar[mid][0]:
                    l = mid + 1
                else:
                    r = mid

        if start < self.calendar[l-1][1]:
            return False
        else:
            self.calendar.insert(l, (start, end))
            return True


# using sorted data structure that allows for insertion in O(log N) time
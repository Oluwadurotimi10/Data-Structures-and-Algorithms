## cleaner
# Leetcode 1029

# TC: O(nlogn), SC: O(1)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        #sorting the difference between cost of tickets per person

        costs = sorted(costs, key=lambda x: x[0] - x[1])

        n = len(costs)//2
        min_cost = 0

        for i in range(n):
            min_cost += costs[i][0] + costs[n+i][1]

        return min_cost
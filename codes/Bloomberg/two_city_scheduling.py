# Leetcode 1029

# TC: O(nlogn), SC: O(1)
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    # sorting the costs based on the cost difference to go to the two cities
    costs = sorted(costs, key=lambda x: x[0] - x[1])
    min_cost = 0

    # taking the first half to go to city A, since if it is negative, the bigger the negative
    # value shows how much we will save to send the person to city A instead of B while if
    # positive value, show how much more it will cost to go to city A rather than B. So it is
    # advisable for the first n ppl after sorting to go to city A, since it show that we are
    # saving more going to A and the last n going to B for the same reason.

    n_people = len(costs) // 2
    for cost in costs[:n_people]:
        min_cost += cost[0]

    for cost in costs[n_people:]:
        min_cost += cost[1]

    return min_cost

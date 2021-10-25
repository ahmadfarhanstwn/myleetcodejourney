class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : (-abs(x[0]-x[1]),min(x[0],x[1])))
        index = output = 0
        n = len(costs)/2
        city = {0 : 0, 1: 0}
        while city[0] < n and city[1] < n:
            output += min(costs[index])
            city[costs[index].index(min(costs[index]))] += 1
            index += 1
        remain = 1 if city[0] >= city[1] else 0
        while index < len(costs):
            output += costs[index][remain]
            index += 1
        return output
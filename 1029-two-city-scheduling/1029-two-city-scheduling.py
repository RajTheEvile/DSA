class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        c=0
        costs.sort(key = lambda x: x[0]-x[1])
        x=len(costs)
        for i in range(x):
            if i<x//2:
                c+=costs[i][0]
            else:
                c+=costs[i][1]
        return c
                
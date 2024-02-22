class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sortedcost = sorted(costs,key = lambda x:x[0]-x[1])
        _sum = 0
        for i in range(0,(len(sortedcost))//2):
            _sum += sortedcost[i][0]
        for i in range((len(sortedcost))//2,len(sortedcost)):
            _sum += sortedcost[i][1]
        return _sum
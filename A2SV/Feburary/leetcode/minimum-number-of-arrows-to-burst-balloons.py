class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        arrows = 0
        maximum = points[0][1]
        
        for i in range(len(points)-1):
            if maximum < points[i+1][0]:
                arrows += 1
                maximum = points[i+1][1]
        return arrows+1

        
        
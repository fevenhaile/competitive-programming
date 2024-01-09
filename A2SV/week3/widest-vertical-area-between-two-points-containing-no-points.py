class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width = points[1][0] - points[0][0]
        for i in range(len(points)-1):
            x = points[i+1][0] - points[i][0]
            max_width = max(max_width,x)
        return max_width

        
        
class Solution:
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)  
        return len([val for index, val in enumerate(sorted_heights) if sorted_heights[index] != heights[index]])
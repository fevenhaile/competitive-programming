class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        # Calculate the initial sum of the first k elements
        windowSum = sum(cardPoints[:k])
        maxScore = windowSum
        
        # Slide the window from left to right
        for i in range(k):
            windowSum -= cardPoints[k - i - 1]
            windowSum += cardPoints[n - i - 1]
            maxScore = max(maxScore, windowSum)
        
        return maxScore
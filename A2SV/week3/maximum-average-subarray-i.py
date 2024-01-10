class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        sums = sum(nums[:k])
        average = sums/k
        for i in range(len(nums)-k):
            sums -= nums[i]
            sums += nums[i+k]
            average = max(average,sums/k)
           
        return average
        
        
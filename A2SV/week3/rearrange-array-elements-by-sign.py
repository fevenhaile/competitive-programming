class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        result = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                positives.append(nums[i])
            else:
                negatives.append(nums[i])
        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
        return result
      

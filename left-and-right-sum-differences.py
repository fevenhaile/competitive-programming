class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefixsum = [0]

        
        totalsum=sum(nums)
        answer=[]
        for i in range(len(nums)):
            prefixsum.append(nums[i] + prefixsum[-1])
            rightsum = totalsum-prefixsum[i+1]
            answer.append(abs(rightsum-prefixsum[i] ))
        return answer
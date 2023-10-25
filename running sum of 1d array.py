class Solution(object):
    def runningSum(self, nums):
        newarray=[]
        prefixsum=0

        for i in nums:
            prefixsum+=i
            newarray.append(prefixsum)
        return newarray
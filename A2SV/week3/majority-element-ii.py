from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        stack = []
        dic = Counter(nums)
        print(dic)
        for key,value in dic.items():
            dic[key] = value
            if value > len(nums)//3:
                stack.append(key)
        return stack
        
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            runner = i
            visited = set()
            flag = (nums[i] > 0)
            while (nums[runner] > 0) == flag and (n + runner + nums[runner]) % n != runner:
                runner = (n + runner + nums[runner]) % n
                if runner in visited:
                    return True
                
                visited.add(runner)
            # runner = i
            # visited = set()
            # while nums[runner] < 0 and (n + runner + nums[runner]) % n != runner:
            #     runner = (n + runner + nums[runner]) % n
            #     if runner in visited:
            #         return True
                
            #     visited.add(runner)


        return False
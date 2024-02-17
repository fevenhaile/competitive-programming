class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        pre = 0
        cnt = [0] * (n + 1)
        cnt[0] = 1
        for i in range(n):
            pre += nums[i] & 1
            if pre >= k:
                ans += cnt[pre - k]
            cnt[pre] += 1
        return ans
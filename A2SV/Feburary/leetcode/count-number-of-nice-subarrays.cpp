class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;
        int pre = 0;
        vector<int> cnt(n + 1, 0);
        cnt[0] = 1;
        for (int i = 0; i < n; i++)
        {
            pre += (nums[i] & 1);
            if (pre >= k)
            {
                ans += cnt[pre - k];
            }
            cnt[pre] += 1;
        }
        return ans;
    }
};
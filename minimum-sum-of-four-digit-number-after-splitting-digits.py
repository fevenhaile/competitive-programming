class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int,sorted(str(num),reverse=True)))
        ans1=0
        ans2=0
        pos=0

        for i in range (len (num)):
            if i % 2 == 0:
                ans1 += num[i] * 10**pos
            else:
                ans2 += num[i] * 10**pos
                pos += 1
        return ans1+ans2
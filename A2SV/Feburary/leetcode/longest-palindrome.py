class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        count = 0
        flag =0
        print(dic)
        for i in dic :
            if dic[i] % 2 == 0:
                count += dic[i]
            else:
                flag=1
                count += (dic[i] -1)
        return count+1 if flag else count
        
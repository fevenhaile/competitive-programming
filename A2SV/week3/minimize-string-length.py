class Solution:
    def minimizedStringLength(self, s: str) -> int:
        mylist = list(s)
        myset = set(mylist)
        return len(myset)

               
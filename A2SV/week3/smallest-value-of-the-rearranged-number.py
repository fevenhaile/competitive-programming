class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            mylist = list(str(num))
            mylist.sort()
            if mylist[0] == "0":
                for i in range(len(mylist)):
                    if mylist[i] != "0":
                        mylist[0], mylist[i] = mylist[i], mylist[0]
                        break
                return int("".join(mylist))
            return int("".join(mylist))
            
        else:
            num = abs(num)
            mylist = list(str(num))
            rev = sorted(mylist, reverse=True)
            val = int("".join(rev))
            return -val

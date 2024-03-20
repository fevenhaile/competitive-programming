class Solution:
    def numberOfWays(self, s: str) -> int:
        #  for 010
        # create a prefix that counts the number of 0's
        l = [int(i) for i in s]
        print(l)
        prefix = [0] * (len(l)+1)
        for i in range(len(l)):
            prefix[i+1] = prefix[i] + (l[i] == 0)
        count = 0 
        for i in range(len(l)):
            if l[i] == 1:
                count += prefix[i] * (prefix[-1] - prefix[i+1])
        print(count)

        # to count the number of ones in an array
        for i in range(len(l)):
            prefix[i+1] = prefix[i] + (l[i] == 1)
        count1 = 0 
        for i in range(len(l)):
            if l[i] == 0:
                count1 += prefix[i] * (prefix[-1] - prefix[i+1])
        print(count1)
        return count+count1


        


        # for i in range(len(zerone)):


        
        
        
        #If your current number is 1, then all the 0s on the LEFT can be combined (multiplied) 
        #    with all the 0s from RIGHT.
        # If your current number is 0, then all the 1s on the LEFT can be combined 
        #   with all the 1s from RIGHT.
        # Count the 1s/zeroes.
        # Traverse the string again, keeping track of how many 1s/0s you have 
        #   sofar. Multiple the LEFT and RIGHT count, depending on current number.
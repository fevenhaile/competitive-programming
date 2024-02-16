class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # how do i update the frequency everytime
        dic  = {}
        minimum = len(cards)
        
        if len(cards) == len(set(cards)):
            return -1
        
        for i in range(len(cards)):
            if cards[i] not in dic:
                dic[cards[i]] = [i]
            else:
                dic[cards[i]].append(i)
                cardnum = (dic[cards[i]][-1] - dic[cards[i]][-2]) + 1
                minimum = min(minimum,cardnum)
        
        return minimum

                

        
          
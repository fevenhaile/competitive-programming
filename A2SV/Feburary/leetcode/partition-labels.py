class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # saving the first and the last occurence of the letters
        reversed = s[::-1]
        dic = {}
        l = 0
        answer = []
        result = []
        maximum = 0
        for i ,j in enumerate (s):
            dic[j] = i
        
        # # for i in range(len(reversed)):
        #     if reversed[i] not in dic:
        #         dic[reversed[i]] = len(reversed) -1-i
        
        p=-1
        for i in range(len(s)):
            maximum = max(maximum,dic[s[i]])
            if i == maximum:
                result.append(i-p)
                p=i
        return result
       

        
            
           
            

        


        
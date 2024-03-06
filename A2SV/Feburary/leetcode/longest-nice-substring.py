class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        dic={}

        for i in range(len(s)):
            possible  = set()
            impossible = set() 
            
            for j in range(i,len(s)):
                
                if ord(s[j]) > 96:
                    char = s[j].upper()
                else:
                    char = s[j].lower()

                if char in possible:
                    
                    if char in impossible:
                        impossible.remove(char)
                else:
                    
                    impossible.add(s[j])
                possible.add(s[j])
                if not impossible and j-i+1 not in dic:
                    dic[j-i+1] = s[i:j+1]
                # print(dic)
        return dic[max(dic)] if dic else  ""
        
 
        
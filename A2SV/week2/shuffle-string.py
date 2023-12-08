class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        shuffelstring = []
        for key,value in zip(s,indices):
            dic[value] = key
        sorted_dic = dict(sorted(dic.items()))
        for value,key in sorted_dic.items():
            sorted_dic[value] = key
            shuffelstring.append(key)
        return "".join(shuffelstring)
         
            

            
            
    
            

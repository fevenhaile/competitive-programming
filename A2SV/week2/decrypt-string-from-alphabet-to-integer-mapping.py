class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        mylist=[]

        characters = "abcdefghijklmnopqrstuvwxyz"

        dic = {str(index+1):char for index,char in enumerate(characters)}
        i = 0 
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                key = s[i:i+2]
                i+=3
                mylist.append(dic[key])
            else:
                key = s[i]
                i+=1
                mylist.append(dic[key])


        return ''.join(mylist)
        
            
            
        
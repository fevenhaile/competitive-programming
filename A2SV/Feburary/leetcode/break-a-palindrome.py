class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pali = list(palindrome)

        if len(pali) == 1:
            return ''
        all_a = 0
        for i in range(0,((len(pali)//2)+1)):
            if pali[i] == 'a':
                all_a += 1
            
        if palindrome == 'aa':
            return 'ab'
        if all_a == len(pali)//2:
            pali[-1] = 'b'
        else:
            for i in range(0,((len(pali)//2))+1):
                if pali[i] != 'a':
                    pali[i] = 'a'
                    break
        return ''.join(pali)
        


            
            

        
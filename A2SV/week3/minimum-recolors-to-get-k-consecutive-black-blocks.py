class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        dic = Counter(window)
        
        minim = float('inf')
        for i in range(len(blocks)-k):
            minim = min(minim,dic["W"])

            dic[blocks[i+k]] += 1
            dic[blocks[i]] -= 1
        minim = min(minim,dic["W"])
        
           
        return minim
        



        
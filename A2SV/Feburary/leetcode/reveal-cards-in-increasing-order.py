class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0] * len(deck)
        queue = deque([i for i in range(len(deck))])
        i = 0
        while queue:
            x = queue.popleft()
            ans[x] = deck[i]
            i+=1
            if queue:
                y = queue.popleft()
                queue.append(y)
        return ans


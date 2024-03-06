class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x = bisect_right(letters,target)
        if x == len(letters):
            x = 0
        return letters[x]
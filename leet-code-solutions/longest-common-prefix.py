from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort(key=len)
        shortest_string = strs[0]

        for i in range(len(shortest_string)):
            for j in range(1, len(strs)):
                if strs[j][i] != shortest_string[i]:
                    return shortest_string[:i]

        return shortest_string
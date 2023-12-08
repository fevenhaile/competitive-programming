from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Create dictionaries to store the counts of losses and wins for each player
        losers = {}
        winners = {}

        # Iterate over each match in the list of matches
        for i in matches:
            loser = i[1]
            winner = i[0]

            # Update the count of losses for the loser
            losers[loser] = losers.get(loser, 0) + 1

            # Update the count of wins for the winner
            winners[winner] = winners.get(winner, 0) + 1

        # Create a list to store the final result
        ans = [[], []]

        # Iterate over the players in the winners dictionary
        for player in winners:
            # Check if the player has zero losses
            if losers.get(player, 0) == 0:
                # Append the player to the list of players with zero losses
                ans[0].append(player)

        # Iterate over the players in the losers dictionary
        for player in losers:
            # Check if the player has exactly one loss
            if losers.get(player, 0) == 1:
                # Append the player to the list of players with exactly one loss
                ans[1].append(player)

        # Sort both lists in the result in ascending order
        ans[0].sort()
        ans[1].sort()

        # Return the final result
        return ans
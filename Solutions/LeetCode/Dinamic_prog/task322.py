from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        count_coins = [float('inf')] * (amount+1)
        count_coins[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    count_coins[i] = min(count_coins[i-coin]+1, count_coins[i])
        
        return count_coins[amount] if count_coins[amount] != float('inf') else -1
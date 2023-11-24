class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        default_value = amount + 1
        coins_needed = [default_value] * (amount + 1)
        coins_needed[0] = 0

        for current_amount in range(1, len(coins_needed)):
            for coin in coins:
                if current_amount - coin >= 0:
                    coins_needed[current_amount] = min(1 + coins_needed[current_amount - coin], coins_needed[current_amount])

        if coins_needed[amount] == default_value:
            return -1
        return coins_needed[amount]
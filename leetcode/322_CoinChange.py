class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        possible_paths = deque()
        visited_amounts = set()
        possible_paths.append(amount)
        visited_amounts.add(amount)

        numbers_of_coins = 0
        while possible_paths:
            numbers_of_coins += 1
            for _ in range(len(possible_paths)):
                current_amount = possible_paths.popleft()

                for c in coins:
                    next_amount = current_amount - c
                    if next_amount == 0:
                        return numbers_of_coins
                    if next_amount not in visited_amounts and next_amount > 0:
                        possible_paths.append(next_amount)
                        visited_amounts.add(next_amount)

        return -1


'''
coinChange([1,2,5], 11)
min(coinChange([1,2,5], 10), coinChange([1,2,5], 9), coinChange([1,2,5], 6))

coinChange([1,2,5], 10)
min(coinChange([1,2,5], 9), coinChange([1,2,5], 7), coinChange([1,2,5], 5))

coinChange([1,2,5], 5)
min(coinChange([1,2,5], 4), coinChange([1,2,5], 3), coinChange([1,2,5], 0))

11 [1,2,5]
[10, 9, 6] -> [9, 8, 5, 8, 7, 4, 5, 4, 1] -> (9, 8, 5, 4, 1) -> (8, 7, 6, 4, 3, 0)
[5, 4, 1]
[0, 2, 0]

32 [1,2,5]
[]
'''
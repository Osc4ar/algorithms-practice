class Solution:
    '''
    We need to buy in the smallest possible value and sell in the highest value after buying

    The bigger the difference between them the better
     
    diff = 5
        M           *
    [7, 1, 5, 3, 6, 4]

    We can iterate the array and check two things:
    1. If the value is smaller than our smallest value, save it as the new smallest
    2. If it is bigger, get the difference between the two numbers
    3. If the difference is bigger than the previous one, save it
    4. Repeat for every price in the list, return the max diff
    '''
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                profit = max(profit, diff)

        return profit

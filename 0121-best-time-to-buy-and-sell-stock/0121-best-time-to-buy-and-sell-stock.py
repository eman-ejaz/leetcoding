class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0
        l, r = 0, 1

        while r < len(prices):
            diff = prices[r] - prices[l]

            if diff < 0:
                l += 1
                r += 1
            else:
                max_p = max(max_p, diff)
                r += 1
            
            if r < len(prices) and prices[r] < prices[l]:
                l = r
        return max_p



        # max_profit = 0

        # i = 0

        # while i < len(prices):
        #     if i + 1 < len(prices) and prices[i] < prices[i + 1]:
        #         j = i + 1

        #         while j < len(prices):
        #             profit = prices[j] - prices[i]

        #             if profit >= 0:
        #                 max_profit = max(max_profit, profit)
        #             j += 1

        #     i += 1

        # return max_profit

    # optimized
        max_profit = 0
        min_price = float('inf')

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] - min_price > 0:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit
            
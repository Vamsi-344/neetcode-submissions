class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitSoFar = -1
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > profitSoFar:
                    profitSoFar = prices[j] - prices[i]
                else:
                    continue
        return profitSoFar
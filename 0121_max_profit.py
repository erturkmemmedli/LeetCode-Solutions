class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        minimum = 0
        for i in range(1, len(prices)):
            if prices[i] <= prices[minimum]:
                minimum = i
            else:
                dp[i] = prices[i] - prices[minimum]
        return max(dp)

# Alternative solution

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if dp[i-1] + prices[i] - prices[i-1] >= 0:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = 0
        return max(dp)

# Alternative solution

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
                maximum = prices[i]
            else:
                maximum = prices[i]
                result = max(result, maximum - minimum)
        return result

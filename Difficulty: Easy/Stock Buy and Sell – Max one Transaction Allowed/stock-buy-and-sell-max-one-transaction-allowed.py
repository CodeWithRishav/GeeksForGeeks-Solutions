class Solution:

    def maximumProfit(self, prices):
        # Initialize the minimum buy price as the first price in the list
        buy_price = prices[0]
        # Initialize the maximum profit as 0
        max_profit = 0

        # Iterate through the list of prices starting from the second price (index 1)
        for i in range(1, len(prices)):
            # Update the maximum profit if the current profit (prices[i] - buy_price) is greater
            max_profit = max(max_profit, prices[i] - buy_price)
            # Update the minimum buy price if the current price is lower
            buy_price = min(buy_price, prices[i])

        # Return the maximum possible profit
        return max_profit


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends
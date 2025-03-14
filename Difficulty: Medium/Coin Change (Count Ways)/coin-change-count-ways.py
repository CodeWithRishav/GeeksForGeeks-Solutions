class Solution:

    def count(self, coins, sum):
        n = len(coins)

        # 2d dp array where n is the number of coin
        # denominations and sum is the target sum
        dp = [[0] * (sum + 1) for _ in range(n + 1)]

        # Represents the base case where the target sum is 0,
        # and there is only one way to make change: by not
        # selecting any coin
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(sum + 1):

                # Add the number of ways to make change without
                # using the current coin
                dp[i][j] += dp[i - 1][j]

                if (j - coins[i - 1]) >= 0:

                    # Add the number of ways to make change
                    # using the current coin
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][sum]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends
class Solution:

    def noOfWays(self, m, n, x):

        # Initialize dp array where dp[j] stores
        # the number of ways to get a sum 'j' using 'i' dice
        dp = [0] * (x + 1)

        # Base case: 1 way to get sum 0 (no dice)
        dp[0] = 1

        # Iterate through each dice (i) from 1 to n
        for i in range(1, n + 1):

            # Iterate backwards through all possible sums (j) from x to 1
            # to avoid overwriting results from the previous dice count
            for j in range(x, 0, -1):

                # Reset dp[j] before calculating its new value for the current dice
                dp[j] = 0

                # Loop through all possible dice outcomes (k)
                # If j - k is a valid sum (non-negative), update dp[j]
                for k in range(1, m + 1):
                    if j - k >= 0:
                        dp[j] += dp[j - k]

            # After each dice iteration, set dp[0] to 0
            dp[0] = 0

        # Return the number of ways to get sum 'x' using 'n' dice
        return dp[x]
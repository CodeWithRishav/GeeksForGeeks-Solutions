class Solution:

    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(W + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    pick = 0
                    if wt[i - 1] <= j:
                        pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                    notPick = dp[i - 1][j]
                    dp[i][j] = max(pick, notPick)

        return dp[n][W]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
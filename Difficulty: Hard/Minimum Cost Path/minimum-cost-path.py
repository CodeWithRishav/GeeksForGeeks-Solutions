class Solution:
    
    #Function to return the minimum cost to react at bottom
    #right cell from top left cell.
    def minimumCostPath(self, grid):
        
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in range(m)]
        
        # update the cell cost only via 2 directions
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0):
                    dp[i][j] = grid[i][j]
                if i-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+grid[i][j])
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+grid[i][j])
                  
        # update the cell cost via 4 directions  
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+grid[i][j])
                if i+1 < m:
                    dp[i][j] = min(dp[i][j], dp[i+1][j]+grid[i][j])                    
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+grid[i][j])                  
                if j+1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j+1]+grid[i][j])
                    
        return dp[-1][-1]


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends
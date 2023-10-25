class Solution:
    # Function to solve the knapsack problem
    def knapSack(self, N, W, val, wt):
        # Create a dynamic programming array to store the values
        dp = [0 for i in range(W + 1)] 

        ans = 0

        # Iterate through each weight
        for i in range(W + 1): 
            # Iterate through each item
            for j in range(N): 
                # Check if the weight of the item is less than or equal to the current weight
                if (wt[j] <= i): 
                    # Update the maximum value for the current weight
                    dp[i] = max(dp[i], dp[i - wt[j]] + val[j]) 

        # Return the maximum value for the given weight
        return dp[W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
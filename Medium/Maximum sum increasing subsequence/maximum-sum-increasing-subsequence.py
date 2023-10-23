class Solution:
    def maxSumIS(self, Arr, n):
        dp = [-1]*(n+1)
        
        # Recursive function to find the maximum increasing subsequence sum
        def solve(Arr, i, n, dp):
            if i==n:
                return 0 
            if dp[i] != -1:
                return dp[i]
            
            ans = Arr[i]
            for j in range(i+1,n):
                # Check if the current element is greater than the previous element
                if Arr[i]<Arr[j]:
                    ans = max(ans, Arr[i]+solve(Arr,j,n,dp))
            dp[i] = ans
            return dp[i]
        
        ans = 0
        for i in range(n):
            # Find the maximum increasing subsequence sum starting from each element
            ans = max(ans, solve(Arr,i,n,dp))
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends
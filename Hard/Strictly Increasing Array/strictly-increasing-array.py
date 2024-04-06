#User function Template for python3

class Solution:
    def min_operations(self,nums):
        # Code here
        dp = [1 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and nums[i] - nums[j] >= (i-j):
                    dp[i] = max(dp[i], 1 + dp[j])
        max_ls = max(dp)
        return len(nums) - max_ls
        # Code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends
# Your task is to complete this function
# Finction should return Integer
class Solution:

    #Function to count the number of subsequences.
    def sequenceCount(self,s, t):
        n = len(s)
        m = len(t)
        mod = 10**9+7

        #Creating a DP table.
        dp = [[-1 for i in range(m+1)]for j in range(n+1)]

        #Recursive function to solve the problem.
        def solve(s, t, i, j, dp):
            #Base cases
            if j==len(t):
                dp[i][j] = 1
                return 1 
            if i==len(s):
                dp[i][j] = 0
                return 0

            #If the value is already calculated, return it.
            if dp[i][j] != -1:
                return dp[i][j]

            #If the current characters are not equal, move to next character in s.
            if s[i] != t[j]:
                dp[i][j] = solve(s,t,i+1,j,dp)%mod
                return dp[i][j]
            #If the current characters are equal, consider two cases:
            #1. Include the current character in the subsequence and move to the next character in both s and t.
            #2. Exclude the current character from the subsequence and only move to the next character in s.
            else:
                dp[i][j] = (solve(s,t,i+1,j+1,dp)+solve(s,t,i+1,j,dp)) % mod
                return dp[i][j]

        #Calling the recursive function with initial parameters.
        return solve(s,t,0,0,dp)


#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends
#User function Template for python3

class Solution:
      def largestSubsquare(self, n, a):
        #code here
        n = len(a)
        dp = [[(0, 0)]*(n+1) for _ in range(n+1)]
        
        for r in range(n):
            for c in range(n):
                if a[r][c] == 'X':
                    dp[r+1][c+1] = (dp[r][c+1][0]+1, dp[r+1][c][1]+1)
        

        ans = 0
        for r in range(1, n+1):
            for c in range(1, n+1):
                d = min(dp[r][c])
                while d > ans:
                    left = c-d+1
                    top = r-d+1
                    if dp[r][left][0] >= d and dp[top][c][1] >= d:
                        ans = d
                        break
                    d -= 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends
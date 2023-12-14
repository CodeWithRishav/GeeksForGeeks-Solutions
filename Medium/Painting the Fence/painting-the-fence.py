class Solution:
    def countWays(self,n,k):
        total = k
        same = 0
        diff = k
        mod = int(1e9) + 7
        for i in range(2, n + 1):
            same = diff
            diff = (total % mod * (k - 1) % mod) % mod
            total = (same + diff) % mod
        return total



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends
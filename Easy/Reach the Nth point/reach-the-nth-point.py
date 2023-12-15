#User function Template for python3

class Solution:
    def nthPoint(self,n):
        mod=(10**9)+7
        fib=[0]*(n+1)
        fib[0]=1
        fib[1]=1
        for i in range(2,n+1):
            fib[i]=(fib[i-1]+fib[i-2])%mod
        return fib[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends
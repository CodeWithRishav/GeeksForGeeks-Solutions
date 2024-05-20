#User function Template for python3

class Solution:
    def binpow(self,a,b,m):
        res=1
        while b:
            if b&1:
                res=(res*a)%m
            a=(a*a)%m
            b>>=1
        return res
    def PowMod(self, x, n, m):
        if x==n==m:
            return 0
        return self.binpow(x,n,m)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends
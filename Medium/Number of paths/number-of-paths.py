class Solution:
    def numberOfPaths (self, M, N):
        path = 1;  #initialize path count variable
        MOD = 10**9+7
    
        #iterate from n to m+n-1
        for i in range(N,M+N-1) :
            path = (i*path)%MOD  #multiply path by current value
            inv = pow(i - N + 1, MOD - 2, MOD)
            path = (path * inv)%MOD # Dividing path by (i-N+1)
            
        return path;  #return the path count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends
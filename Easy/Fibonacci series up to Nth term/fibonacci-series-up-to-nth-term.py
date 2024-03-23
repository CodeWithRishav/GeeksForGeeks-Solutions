#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        lst=[]
        lst.append(0)
        lst.append(1)
        for i in range(n-1):
            lst.append((lst[-1]+lst[-2])%(10**9+7))
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends
# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        for c in range(m - 2, -1, -1):
            for r in range(n):
                topRight = M[r - 1][c + 1] if r > 0 else 0
                right = M[r][c + 1]
                bottomRight = M[r + 1][c + 1] if r < n - 1 else 0
                M[r][c] += max(topRight, right, bottomRight)
        ans = 0
        for r in range(n):
            ans = max(ans, M[r][0])
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends
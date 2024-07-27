#User function Template for python3

class Solution:
    def countMin(self, str):
        # code here
        s1 = str
        n = len(str)
        s2 = s1[::-1]
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j]  = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return n-dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends
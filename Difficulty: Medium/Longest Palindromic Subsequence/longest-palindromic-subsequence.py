#User function Template for python3

class Solution:
    # Function to find the length of the longest palindromic subsequence.
    def longestPalinSubseq(self, s):
        n = len(s)
        rev_s = s[::-1]  # Reverse the string to compare with original

        # Creating a dp array with size (n+1) x (n+1).
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Filling up the dp array with the lengths of palindromic subsequences.
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev_s[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Returning the length of the longest palindromic subsequence.
        return dp[n][n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
        print("~")
# } Driver Code Ends